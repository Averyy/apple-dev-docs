# Extending your app’s background execution time

**Framework**: UIKit

Ensure that critical tasks finish when your app moves to the background.

#### Overview

Extending your app’s background execution time ensures that you have adequate time to perform critical tasks. For tasks that require more background time, use [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks).

When your app moves to the background, the system calls your app delegate’s [`applicationDidEnterBackground(_:)`](uiapplicationdelegate/applicationdidenterbackground(_:).md) method. That method has five seconds to perform any tasks and return. Shortly after that method returns, the system puts your app into the suspended state. For most apps, five seconds is enough to perform any crucial tasks, but if you need more time, you can ask UIKit to extend your app’s runtime.

You extend your app’s runtime by calling the [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md) method. Calling this method gives you extra time to perform important tasks. (You can find out the maximum background time available using the [`backgroundTimeRemaining`](uiapplication/backgroundtimeremaining.md) property.) When you finish your tasks, call the [`endBackgroundTask(_:)`](uiapplication/endbackgroundtask(_:).md) method right away to let the system know that you’re done. If you don’t end your tasks in a timely manner, the system terminates your app.

> **Note**:  Don’t wait until your app moves to the background to call the [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md) method. Call the method before performing any long-running task.

 Don’t wait until your app moves to the background to call the [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md) method. Call the method before performing any long-running task.

The following code shows an example that configures a background task so that the app may save data to its server, which could take longer than five seconds. The [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md) method returns an identifier that you must save and pass to the [`endBackgroundTask(_:)`](uiapplication/endbackgroundtask(_:).md) method.

```swift
func sendDataToServer( data : NSData ) {
   // Perform the task on a background queue.
   DispatchQueue.global().async {
      // Request the task assertion and save the ID.
      self.backgroundTaskID = UIApplication.shared.
                 beginBackgroundTask (withName: "Finish Network Tasks") {
         // End the task if time expires.
         UIApplication.shared.endBackgroundTask(self.backgroundTaskID!)
         self.backgroundTaskID = UIBackgroundTaskInvalid
      }
            
      // Send the data synchronously.
      self.sendAppDataToServer( data: data)
            
      // End the task assertion.
      UIApplication.shared.endBackgroundTask(self.backgroundTaskID!)
      self.backgroundTaskID = UIBackgroundTaskInvalid
   }
}
```

> **Note**:  The [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md) method can’t be called from an app extension. To request extra execution time from your app extension, call the [`performExpiringActivity(withReason:using:)`](https://developer.apple.com/documentation/foundation/processinfo/1617030-performexpiringactivity) method of [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo) instead.

 The [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md) method can’t be called from an app extension. To request extra execution time from your app extension, call the [`performExpiringActivity(withReason:using:)`](https://developer.apple.com/documentation/foundation/processinfo/1617030-performexpiringactivity) method of [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo) instead.

## See Also

- [Using background tasks to update your app](using-background-tasks-to-update-your-app.md)
  Configure your app to perform tasks in the background to make efficient use of processing time and power.
- [About the background execution sequence](about-the-background-execution-sequence.md)
  Learn the order in which your custom code is executed when your app moves to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/extending-your-app-s-background-execution-time)*