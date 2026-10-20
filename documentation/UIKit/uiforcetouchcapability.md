# UIForceTouchCapability

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Keys that indicate the availability of 3D Touch on a device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum UIForceTouchCapability
```

```c
enum UIForceTouchCapability : NSInteger;
```

#### Overview

Only certain devices support 3D Touch. On those that do, the user can disable 3D Touch in the Accessibility area in Settings.

## Topics

### Availability options
- [UIForceTouchCapability.unknown](./uiforcetouchcapability/unknown.md)
  The availability of 3D Touch is unknown.
- [UIForceTouchCapability.available](./uiforcetouchcapability/available.md)
  3D Touch is available on the device.
- [UIForceTouchCapability.unavailable](./uiforcetouchcapability/unavailable.md)
  3D Touch isn’t available on the device.
### Initializers
- [init?(rawValue: Int)](./uiforcetouchcapability/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Retrieving the force touch capability traits
- [var forceTouchCapability: UIForceTouchCapability](./uitraitcollection/forcetouchcapability.md)
  The force touch capability value of the trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiforcetouchcapability)*