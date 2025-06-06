# ENActivityFlags

**Framework**: Exposure Notification  
**Kind**: struct

Activities that occur while the app isn’t running.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
struct ENActivityFlags
```

#### Overview

> ❗ **Important**:  This symbol is available in iOS 12.5, and in iOS 13.6 and later.

 This symbol is available in iOS 12.5, and in iOS 13.6 and later.

## Topics

### Initializers
- [init(rawValue: UInt32)](enactivityflags/init(rawvalue:).md)
  Initialize the structure.
### Type Properties
- [static var periodicRun: ENActivityFlags](enactivityflags/periodicrun.md)
  The property that specifies launching the app in the background for periodic operation in iOS 12.5.
- [static var preAuthorizedKeyReleaseNotificationTapped: ENActivityFlags](enactivityflags/preauthorizedkeyreleasenotificationtapped.md)
  The property that specifies launching the app in the foreground to display preauthorized key-release information.
- [static var reserved1: ENActivityFlags](enactivityflags/reserved1.md)
  This property is reserved.
- [static var reserved2: ENActivityFlags](enactivityflags/reserved2.md)
  This property is reserved.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func activate(completionHandler: ENErrorHandler)](enmanager/activate(completionhandler:).md)
  Prepares the manager for use.
- [var activityHandler: ENActivityHandler?](enmanager/activityhandler.md)
  The handler that the framework invokes when the app activates a notification manager.
- [typealias ENActivityHandler](enactivityhandler.md)
  The handler the system invokes to report activities that occurred while the app wasn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ENErrorHandler)](enmanager/setexposurenotificationenabled(_:completionhandler:).md)
  Enables or disables exposure notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enactivityflags)*