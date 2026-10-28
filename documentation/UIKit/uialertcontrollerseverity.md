# UIAlertControllerSeverity

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants for specifying the severity of an alert in apps built with Mac Catalyst.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum UIAlertControllerSeverity
```

```c
enum UIAlertControllerSeverity : NSInteger;
```

## Overview

This enumeration defines the severity options used by the [`severity`](./uialertcontroller/severity.md) property of [`UIAlertController`](./uialertcontroller.md). In apps built with Mac Catalyst, the severity determines the style of the presented alert. A [`UIAlertControllerSeverity.critical`](./uialertcontrollerseverity/critical.md) alert appears with a caution icon, and an alert with a [`UIAlertControllerSeverity.default`](./uialertcontrollerseverity/default.md) severity doesn’t. UIKit ignores the alert severity on iOS.

You should only use the [`UIAlertControllerSeverity.critical`](./uialertcontrollerseverity/critical.md) severity if an alert truly requires special attention from the user. For more information, see the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/macos/windows-and-views/alerts/) on alerts.

## Topics

### Constants
- [UIAlertControllerSeverity.critical](./uialertcontrollerseverity/critical.md)
  Indicates that the system should present the alert using the critical, or caution, style.
- [UIAlertControllerSeverity.default](./uialertcontrollerseverity/default.md)
  Indicates that the system should present the alert using the standard alert style.
### Initializers
- [init?(rawValue: Int)](./uialertcontrollerseverity/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring alert severity
- [var severity: UIAlertControllerSeverity](./uialertcontroller/severity.md)
  Indicates the severity of the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontrollerseverity)*