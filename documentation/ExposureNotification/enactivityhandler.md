# ENActivityHandler

**Framework**: Exposure Notification  
**Kind**: typealias

The handler the system invokes to report activities that occurred while the app wasn’t running.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
typealias ENActivityHandler = (ENActivityFlags) -> Void
```

## Parameters

- `activityFlags`: The flags indicating what activity occured while the app wasn’t running.

## See Also

- [func activate(completionHandler: ((any Error)?) -> Void)](enmanager/activate(completionhandler:).md)
  Prepares the manager for use.
- [var activityHandler: ENActivityHandler?](enmanager/activityhandler.md)
  The handler that the framework invokes when the app activates a notification manager.
- [struct ENActivityFlags](enactivityflags.md)
  Activities that occur while the app isn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ((any Error)?) -> Void)](enmanager/setexposurenotificationenabled(_:completionhandler:).md)
  Enables or disables exposure notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enactivityhandler)*