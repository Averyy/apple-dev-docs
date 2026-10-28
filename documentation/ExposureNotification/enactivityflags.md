# ENActivityFlags

**Framework**: Exposure Notification  
**Kind**: struct  
**Role**: Structure

Activities that occur while the app isn’t running.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
struct ENActivityFlags
```

```c
enum ENActivityFlags : uint32_t;
```

## Overview

> ❗ **Important**:  This symbol is available in iOS 12.5, and in iOS 13.6 and later.

## Topics

### Initializers
- [init(rawValue: UInt32)](./enactivityflags/init%28rawvalue%29.md)
  Initialize the structure.
### Type Properties
- [static var periodicRun: ENActivityFlags](./enactivityflags/periodicrun.md)
  The property that specifies launching the app in the background for periodic operation in iOS 12.5.
- [static var preAuthorizedKeyReleaseNotificationTapped: ENActivityFlags](./enactivityflags/preauthorizedkeyreleasenotificationtapped.md)
  The property that specifies launching the app in the foreground to display preauthorized key-release information.
- [static var reserved1: ENActivityFlags](./enactivityflags/reserved1.md)
  This property is reserved.
- [static var reserved2: ENActivityFlags](./enactivityflags/reserved2.md)
  This property is reserved.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Activating the Manager
- [func activate(completionHandler: ((any Error)?) -> Void)](./enmanager/activate%28completionhandler%29.md)
  Prepares the manager for use.
- [var activityHandler: ENActivityHandler?](./enmanager/activityhandler.md)
  The handler that the framework invokes when the app activates a notification manager.
- [typealias ENActivityHandler](./enactivityhandler.md)
  The handler the system invokes to report activities that occurred while the app wasn’t running.
- [func setExposureNotificationEnabled(Bool, completionHandler: ((any Error)?) -> Void)](./enmanager/setexposurenotificationenabled%28_,completionhandler%29.md)
  Enables or disables exposure notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enactivityflags)*