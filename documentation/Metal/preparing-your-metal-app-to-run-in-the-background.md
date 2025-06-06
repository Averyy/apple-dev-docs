# Preparing Your Metal App to Run in the Background

**Framework**: Metal

Prepare your app to move into the background by pausing future GPU use and ensuring previous work is scheduled.

#### Overview

iOS and tvOS restrict a background app’s access to the GPU, to guarantee foreground app performance. If a Metal command queue tries to schedule command buffers after the app moves in the background, the system prevents those commands from executing. When UIKit notifies you that your app is being suspended or moved into the background, your app must restrict its use of Metal.

For more information on the UIKit app life cycle, see [`Preparing your UI to run in the background`](https://developer.apple.com/documentation/UIKit/preparing-your-ui-to-run-in-the-background).

##### Disable Code That Commits New Command Buffers

When your app is deactivated, stop sending work to Metal. Enable that code only after your app is reactivated.

After the system notifies your app that it’s being deactivated, you’ve some time before the system restricts your app from using Metal. You can schedule additional commands if that work is critical to prepare your app to be in the background state. Similarly, if your app was already in the middle of encoding commands, your app can typically finish the current task before disabling further work. For example, if your app renders frames of animation to the screen, and you receive the notification while you’re encoding commands for a new frame, you can finish encoding that frame before disabling your rendering code.

##### Ensure All Previous Work Is Scheduled for Execution

When UIKit calls your app delegate’s [`applicationDidEnterBackground(_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/applicationDidEnterBackground(_:)) method, make sure Metal has scheduled all command buffers you’ve already committed before your app returns control to the system. On each command queue, if the last command buffer you queued isn’t already scheduled or complete, call [`waitUntilScheduled()`](mtlcommandbuffer/waituntilscheduled().md) to force it to be scheduled.

If you’re in the middle of encoding a new command buffer, you can combine these steps. Finish encoding commands to render the frame and commit the command buffer, then call [`waitUntilScheduled()`](mtlcommandbuffer/waituntilscheduled().md).

After your app moves into the background, if Metal sees a new command buffer from your app, it returns an error, rather than scheduling the command buffer. To test for this error, add a completion handler by calling the [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md) method. In your completion handler, confirm the command buffer is in an error state by checking the following properties:

- The [`status`](mtlcommandbuffer/status.md) property is equal to [`MTLCommandBufferStatus.error`](mtlcommandbufferstatus/error.md)
- The [`error`](mtlcommandbuffer/error.md) property is equal to [`MTLCommandBufferError.Code.notPermitted`](mtlcommandbuffererror-swift.struct/code/notpermitted.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/preparing-your-metal-app-to-run-in-the-background)*