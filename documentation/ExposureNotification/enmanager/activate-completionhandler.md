# activate(completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method

Prepares the manager for use.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
func activate() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func activate() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 and later.

Properties may not be usable until the completion handler reports success.

## Parameters

- `completionHandler`: The completion handler that the framework calls when activation completes.

## See Also

- [var activityHandler: ENActivityHandler?](enmanager/activityhandler.md)
  The handler that the framework invokes when the app activates a notification manager.
- [typealias ENActivityHandler](enactivityhandler.md)
  The handler the system invokes to report activities that occurred while the app wasn’t running.
- [struct ENActivityFlags](enactivityflags.md)
  Activities that occur while the app isn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ((any Error)?) -> Void)](enmanager/setexposurenotificationenabled(_:completionhandler:).md)
  Enables or disables exposure notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/activate(completionhandler:))*