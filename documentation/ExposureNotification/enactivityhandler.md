# ENActivityHandler

**Framework**: Exposure Notification  
**Kind**: typealias  
**Role**: Type Alias

The handler the system invokes to report activities that occurred while the app wasn’t running.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
typealias ENActivityHandler = (ENActivityFlags) -> Void
```

```c
typedef void (^)(enum ENActivityFlags) ENActivityHandler;
```

## Parameters

- `activityFlags`: The flags indicating what activity occured while the app wasn’t running.

## See Also

### Activating the Manager
- [func activate(completionHandler: ((any Error)?) -> Void)](./enmanager/activate%28completionhandler%29.md)
  Prepares the manager for use.
- [var activityHandler: ENActivityHandler?](./enmanager/activityhandler.md)
  The handler that the framework invokes when the app activates a notification manager.
- [struct ENActivityFlags](./enactivityflags.md)
  Activities that occur while the app isn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ((any Error)?) -> Void)](./enmanager/setexposurenotificationenabled%28_,completionhandler%29.md)
  Enables or disables exposure notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enactivityhandler)*