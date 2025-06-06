# applicationDidEnterBackground(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the app is now in the background.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationDidEnterBackground(_ application: UIApplication)
```

## Mentions

- [About the background execution sequence](about-the-background-execution-sequence.md)
- [Extending your app’s background execution time](extending-your-app-s-background-execution-time.md)

#### Discussion

> ❗ **Important**:  If you’re using scenes (see [`Scenes`](scenes.md)), UIKit will not call this method. Use [`sceneDidEnterBackground(_:)`](uiscenedelegate/scenedidenterbackground(_:).md) instead to perform any final tasks. UIKit posts a [`didEnterBackgroundNotification`](uiapplication/didenterbackgroundnotification.md) regardless of whether your app uses scenes.

 If you’re using scenes (see [`Scenes`](scenes.md)), UIKit will not call this method. Use [`sceneDidEnterBackground(_:)`](uiscenedelegate/scenedidenterbackground(_:).md) instead to perform any final tasks. UIKit posts a [`didEnterBackgroundNotification`](uiapplication/didenterbackgroundnotification.md) regardless of whether your app uses scenes.

Use this method to release shared resources, invalidate timers, and store enough app state information to restore your app to its current state in case it’s terminated later. Disable updates to your app’s user interface, and avoid using some types of shared system resources (such as the user’s contacts database). Don’t use OpenGL ES in the background.

Return from [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) as quickly as possible. Your implementation of this method has approximately five seconds to perform any tasks and return. If the method doesn’t return before time runs out, your app is terminated and purged from memory.

If you need additional time to perform any final tasks, request additional execution time from the system by calling [`beginBackgroundTask(expirationHandler:)`](uiapplication/beginbackgroundtask(expirationhandler:).md). Call [`beginBackgroundTask(expirationHandler:)`](uiapplication/beginbackgroundtask(expirationhandler:).md) as early as possible. Because the system needs time to process your request, there’s a chance that the system might suspend your app before that task assertion is granted. For example, don’t call [`beginBackgroundTask(expirationHandler:)`](uiapplication/beginbackgroundtask(expirationhandler:).md) at the very end of your [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method and expect your app to continue running.

Perform any tasks related to adjusting your user interface before [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) exits. Move other tasks (such as saving state) to a concurrent dispatch queue or secondary thread as needed. Because it’s likely any background tasks you start in [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) won’t run until after that method exits, request additional background execution time before starting those tasks. In other words, first call [`beginBackgroundTask(expirationHandler:)`](uiapplication/beginbackgroundtask(expirationhandler:).md) and  run the task on a dispatch queue or secondary thread.

UIKit also posts a [`didEnterBackgroundNotification`](uiapplication/didenterbackgroundnotification.md) around the same time it calls this method to give interested objects a chance to respond to the transition.

For more information about how to transition gracefully to the background, and for information about how to start background tasks, see [`App Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

## Parameters

- `application`: Your singleton app object.

## See Also

- [func applicationDidBecomeActive(UIApplication)](uiapplicationdelegate/applicationdidbecomeactive(_:).md)
  Tells the delegate that the app has become active.
- [func applicationWillResignActive(UIApplication)](uiapplicationdelegate/applicationwillresignactive(_:).md)
  Tells the delegate that the app is about to become inactive.
- [func applicationWillEnterForeground(UIApplication)](uiapplicationdelegate/applicationwillenterforeground(_:).md)
  Tells the delegate that the app is about to enter the foreground.
- [func applicationWillTerminate(UIApplication)](uiapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate when the app is about to terminate.
- [class let didBecomeActiveNotification: NSNotification.Name](uiapplication/didbecomeactivenotification.md)
  A notification that posts when the app becomes active.
- [class let didEnterBackgroundNotification: NSNotification.Name](uiapplication/didenterbackgroundnotification.md)
  A notification that posts when the app enters the background.
- [class let willEnterForegroundNotification: NSNotification.Name](uiapplication/willenterforegroundnotification.md)
  A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [class let willResignActiveNotification: NSNotification.Name](uiapplication/willresignactivenotification.md)
  A notification that posts when the app is no longer active and loses focus.
- [class let willTerminateNotification: NSNotification.Name](uiapplication/willterminatenotification.md)
  A notification that posts when the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidenterbackground(_:))*