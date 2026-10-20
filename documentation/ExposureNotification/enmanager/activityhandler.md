# activityHandler

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The handler that the framework invokes when the app activates a notification manager.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var activityHandler: ENActivityHandler? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) ENActivityHandler activityHandler;
```

#### Discussion

When the app launches, it creates an [`ENManager`](../enmanager.md) instance, sets this handler, and then activates the manager.

## See Also

### Activating the Manager
- [func activate(completionHandler: ((any Error)?) -> Void)](./activate%28completionhandler%29.md)
  Prepares the manager for use.
- [typealias ENActivityHandler](../enactivityhandler.md)
  The handler the system invokes to report activities that occurred while the app wasn’t running.
- [struct ENActivityFlags](../enactivityflags.md)
  Activities that occur while the app isn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ((any Error)?) -> Void)](./setexposurenotificationenabled%28_,completionhandler%29.md)
  Enables or disables exposure notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/activityhandler)*