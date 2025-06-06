# activityHandler

**Framework**: Exposure Notification  
**Kind**: property

The handler that the framework invokes when the app activates a notification manager.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var activityHandler: ENActivityHandler? { get set }
```

#### Discussion

When the app launches, it creates an [`ENManager`](enmanager.md) instance, sets this handler, and then activates the manager.

## See Also

- [func activate(completionHandler: ENErrorHandler)](enmanager/activate(completionhandler:).md)
  Prepares the manager for use.
- [typealias ENActivityHandler](enactivityhandler.md)
  The handler the system invokes to report activities that occurred while the app wasn’t running.
- [struct ENActivityFlags](enactivityflags.md)
  Activities that occur while the app isn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ENErrorHandler)](enmanager/setexposurenotificationenabled(_:completionhandler:).md)
  Enables or disables exposure notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/activityhandler)*