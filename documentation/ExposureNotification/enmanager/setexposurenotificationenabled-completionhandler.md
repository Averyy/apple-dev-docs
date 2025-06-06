# setExposureNotificationEnabled(_:completionHandler:)

**Framework**: Exposure Notification  
**Kind**: method

Enables or disables exposure notification.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
func setExposureNotificationEnabled(_ enabled: Bool) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setExposureNotificationEnabled(_ enabled: Bool) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func setExposureNotificationEnabled(_ enabled: Bool) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

> ❗ **Important**:  This method is available in iOS 12.5, and in iOS 13.5 and later.

 This method is available in iOS 12.5, and in iOS 13.5 and later.

If the user hasn’t authorized exposure notification, this method displays a user dialog requesting consent.

> **Note**:  Using this method to disable exposure notification stops scanning and Bluetooth advertising, but diagnosis keys and data remain.

 Using this method to disable exposure notification stops scanning and Bluetooth advertising, but diagnosis keys and data remain.

## Parameters

- `enabled`: A Boolean that enables or disables exposure notification.
- `completionHandler`: The completion handler that the framework calls once exposure notification is enabled or disabled.

## See Also

- [func activate(completionHandler: ENErrorHandler)](enmanager/activate(completionhandler:).md)
  Prepares the manager for use.
- [var activityHandler: ENActivityHandler?](enmanager/activityhandler.md)
  The handler that the framework invokes when the app activates a notification manager.
- [typealias ENActivityHandler](enactivityhandler.md)
  The handler the system invokes to report activities that occurred while the app wasn’t running.
- [struct ENActivityFlags](enactivityflags.md)
  Activities that occur while the app isn’t running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/setexposurenotificationenabled(_:completionhandler:))*