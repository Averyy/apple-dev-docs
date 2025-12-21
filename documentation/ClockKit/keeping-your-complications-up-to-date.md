# Keeping your complications up to date

**Framework**: ClockKit

Replace or extend the data in your complication’s timeline.

#### Overview

When you have new data for your watch app, you can replace or extend your complication’s timeline. Call one of the following complication server methods to update the timeline:

In either case, ClockKit instantiates your complication’s data source and requests the new data.

A watchOS app provides several opportunities to update your complication’s timeline. No matter what method you use, keep your watchOS app, appʼs snapshot, notifications, and complications in a consistent state. Also, make sure to update your complication when you update your app’s data. If you receive a push notification with new data, update the app and your complication, and schedule a new screenshot.

> ❗ **Important**:  If the system launches your app in the background (for example, in response to a background download, task, or HealthKit observer query), your complication server’s [`activeComplications`](clkcomplicationserver/activecomplications.md) property may not contain a valid value. If this property is `nil`, the server is still connecting to the active complications on the watch face. For more information on safely accessing the list of active complications, see [`activeComplications`](clkcomplicationserver/activecomplications.md).

##### Update When Your App Runs

If the user’s actions affect your complications, call the [`reloadTimeline(for:)`](clkcomplicationserver/reloadtimeline(for:).md) or [`extendTimeline(for:)`](clkcomplicationserver/extendtimeline(for:).md) method to update them. You can also use active runtime as an opportunity to refresh the complications, even when the user is doing something else. For example, you could try to quickly download data or transfer data from the iOS device while your app is actively running.

Don’t rely on this strategy as the primary way to update your data. You can’t predict when the user will launch your app, and any download, transfer, or update actions that don’t finish while the app is running will need to schedule background tasks. Still, taking advantage of these runtime opportunities can keep your app and complications refreshed.

##### Use Background Url Sessions

Use background URL sessions to download updated data from a server. The system triggers a background task after the download completes, and you can use this task to set up your next download, keeping your app up to date. The system automatically throttles the downloads as needed to preserve battery life. To schedule a background URL session, start by creating a background session configuration.

```swift
let config = URLSessionConfiguration.background(withIdentifier: myRequestID)
config.isDiscretionary = true
config.sessionSendsLaunchEvents = true
```

Setting the [`isDiscretionary`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/isDiscretionary) property to [`true`](https://developer.apple.com/documentation/Swift/true) tells the system to wait for optimal conditions to perform the transfer, such as when the device is plugged in or connected to Wi-Fi. Setting [`sessionSendsLaunchEvents`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/sessionSendsLaunchEvents) to [`true`](https://developer.apple.com/documentation/Swift/true) tells the system to launch your app when the download task completes. This is the default for background configurations.

Next, create the session and use the session to schedule a background download task.

```swift
let urlSession = URLSession(configuration: config,
                            delegate: self,
                            delegateQueue: nil)

let backgroundTask = urlSession.downloadTask(with: url)
backgroundTask.earliestBeginDate = Date().addingTimeInterval(15 * 60)
```

Be sure to assign a [`URLSessionDownloadDelegate`](https://developer.apple.com/documentation/Foundation/URLSessionDownloadDelegate) to the session. Setting the `delegateQueue` to `nil` causes the system to call the delegate methods on an anonymous background thread. Also, use the tasks’s [`earliestBeginDate`](https://developer.apple.com/documentation/Foundation/URLSessionTask/earliestBeginDate) property to schedule the download for the future. If your app’s data isn’t currently up to date, you can schedule the initial download to begin immediately, but subsequent updates should be scheduled for a future date.

The system limits the number of background download tasks you can perform; however, if you have an active complication on the watch face, you can safely schedule four download tasks an hour.

Finally, call [`resume()`](https://developer.apple.com/documentation/Foundation/URLSessionTask/resume()) to schedule the download task.

```swift
backgroundTask.resume()
```

The download continues, even if your app isn’t active. When the download completes, the system launches your app, if necessary. If your app terminated, you need to reconnect to the URL session to receive the download.

To reconnect, create a new URL session using the same configuration identifier. The system then calls that session delegate’s [`urlSession(_:downloadTask:didFinishDownloadingTo:)`](https://developer.apple.com/documentation/Foundation/URLSessionDownloadDelegate/urlSession(_:downloadTask:didFinishDownloadingTo:)) method.

If your app is running in the background, the system also calls your [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-92ulv) method, passing a [`WKURLSessionRefreshBackgroundTask`](https://developer.apple.com/documentation/WatchKit/WKURLSessionRefreshBackgroundTask) object.  It gives your app a maximum of 4 seconds of CPU time which you can use over 15 seconds of wall time. In general, your app should request the next background download task before it begins processing the downloaded data—just in case those tasks exceed the time limits.

Use the download delegate method to access the data and update your app and complication, then call the background task’s [`setTaskCompletedWithSnapshot(_:)`](https://developer.apple.com/documentation/WatchKit/WKRefreshBackgroundTask/setTaskCompletedWithSnapshot(_:)) method and pass true to update your app’s snapshot.

The system calls the following delegate methods in this order:

1. If your app is running in the background, the system calls your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-92ulv) method. Be sure to save the completion handler.
2. If the download succeeds, the system calls your session delegate’s [`urlSession(_:downloadTask:didFinishDownloadingTo:)`](https://developer.apple.com/documentation/Foundation/URLSessionDownloadDelegate/urlSession(_:downloadTask:didFinishDownloadingTo:)) method. Process the downloaded data here.
3. Regardless, the system calls your URL session delegate’s [`urlSession(_:task:didCompleteWithError:)`](https://developer.apple.com/documentation/Foundation/URLSessionTaskDelegate/urlSession(_:task:didCompleteWithError:)) method. If you are running in the background, be sure to call your background task’s completion handler here.

> **Note**:  The system calls the URL session delegate method whether your app is running in the background or the foreground; however, the [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-92ulv) method is only called when your app is running in the background.

For more information, see [`Downloading files in the background`](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background) and [`WKURLSessionRefreshBackgroundTask`](https://developer.apple.com/documentation/WatchKit/WKURLSessionRefreshBackgroundTask).

##### Use Background Observer Queries

In watchOS 8 and later, HealthKit supports background observer queries. Background observer queries share a budget with [`WKApplicationRefreshBackgroundTask`](https://developer.apple.com/documentation/WatchKit/WKApplicationRefreshBackgroundTask) tasks. Your app can receive four updates (or background app refresh tasks) an hour, as long as it has a complication on the active watch face.

Start by enabling the HealthKit capability’s background delivery.

![A screenshot of the HealthKit capability with Background Delivery enabled.](https://docs-assets.developer.apple.com/published/06d50f729dbf07ecdfa635f3d3fcb557/media-3897474%402x.png)

Next, register to recieve updates in the background by calling the HealthKit store’s [`enableBackgroundDelivery(for:frequency:withCompletion:)`](https://developer.apple.com/documentation/HealthKit/HKHealthStore/enableBackgroundDelivery(for:frequency:withCompletion:)) method.

```swift
// Create the caffeine type.
let caffeineType = HKObjectType.quantityType(forIdentifier: .dietaryCaffeine)!

// Set up the background delivery rate.
store.enableBackgroundDelivery(for: caffeineType,
                                  frequency: .immediate) { success, error in
    guard success else {
        self.logger.error("Unable to set up background delivery from HealthKit: \(error!.localizedDescription)")
        fatalError()
    }
}
```

Then create and execute an observer query.

```swift
// Set up the observer query.
backgroundObserver =
HKObserverQuery(sampleType: caffeineType, predicate: nil)
{ (query: HKObserverQuery, completionHandler: @escaping () -> Void, error: Error?) in
    // Query for actual updates here.
    // When you're done processing the changes, be sure to call the completion handler.
    completionHandler()
}

// If you successfully created the query,  execute it.
if let query = backgroundObserver {
    store.execute(query)
}
```

When you have an active observer query, HealthKit wakes your app when the store receives updates to samples matching the query. HealthKit notifies your app at most once per time period defined by the frequency you specified when registering.

To ensure that your app recieves updates, create and execute the observer query soon after your app launches. For example, in your extension delegate’s [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/applicationDidFinishLaunching()) method. For more information, see [`Executing Observer Queries`](https://developer.apple.com/documentation/HealthKit/executing-observer-queries).

##### Schedule Background Tasks

You can schedule background tasks to update your watchOS content periodically. This strategy works best when your data changes at predictable times. Call your extension’s [`scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](https://developer.apple.com/documentation/WatchKit/WKExtension/scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)) method to trigger a [`WKApplicationRefreshBackgroundTask`](https://developer.apple.com/documentation/WatchKit/WKApplicationRefreshBackgroundTask), in which the system launches your app in the background and calls your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-92ulv) method.

During the background task, you can gather updated data from the device. For example, you could perform a HealthKit query for new samples, or check the user’s current location using Core Location. When you’re done, call the background task’s [`setTaskCompletedWithSnapshot(_:)`](https://developer.apple.com/documentation/WatchKit/WKRefreshBackgroundTask/setTaskCompletedWithSnapshot(_:)) method and pass true to update your app’s snapshot.

The system carefully budgets background refresh tasks. You can schedule only one refresh task at a time. If you have a complication on the active watch face, you can safely schedule four refresh tasks a hour.

Also, when the system call your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/handle(_:)-92ulv) method, it gives your app a maximum of 4 seconds of CPU processing time, which you can use over 15 seconds of elapsed real time. In general, set up your requests for the next background task before you begin requesting and processing data—just in case those tasks exceed the time limits.

##### Send Push Notifications

Push notifications let you process data on your server, and update the watch as soon as the data is available. This update method allows you to perform complex, time-consuming data-gathering tasks that wouldn’t otherwise be practical on Apple Watch. It also lets you send an update as soon as the data is available, instead of waiting for a periodic refresh task.

To update your watchOS content from your server, send a [`complication`](https://developer.apple.com/documentation/PushKit/PKPushType/complication) push notification. For watchOS 6 and later, send the push notification directly to Apple Watch. For watchOS 5 and earlier, you must send it to the iOS companion instead. The system limits you to 50 push notifications per day. For more information on setting up and sending push notifications, see [`PushKit`](https://developer.apple.com/documentation/PushKit).

##### Transfer Data From Ios

Alternatively, if your watchOS app has a companion iOS app, you can gather the data in the iOS app, and then transmit that data to Apple Watch. However, this update strategy tethers the watch to the companion iPhone. You can’t update the complication if the user ventures out without their phone, a circumstance that can result in out-of-date or inaccurate complications. Also, like push notifications, the system limits you to 50 complication transfers a day.

For more information on sending updates from the phone, see the [`Watch Connectivity`](https://developer.apple.com/documentation/WatchConnectivity) framework’s [`transferCurrentComplicationUserInfo(_:)`](https://developer.apple.com/documentation/WatchConnectivity/WCSession/transferCurrentComplicationUserInfo(_:)) method.

## See Also

- [Creating complications for your watchOS app](creating-complications-for-your-watchos-app.md)
  Set up and implement complications for your watchOS app.
- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Creating a timeline entry](creating-a-timeline-entry.md)
  Package your app-specific data into a template and create a timeline entry for that template.
- [Loading future timeline events](loading-future-timeline-events.md)
  Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.
- [Building complications with SwiftUI](building-complications-with-swiftui.md)
  Design the appearance of a graphic complication using SwiftUI.
- [Displaying progress views and gauges](displaying-progress-views-and-gauges.md)
  Add rich visual data to your SwiftUI complications with progress views and gauges.
- [Adding text to a complication](adding-text-to-a-complication.md)
  Use text in SwiftUI complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/keeping-your-complications-up-to-date)*