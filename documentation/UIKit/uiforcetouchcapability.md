# UIForceTouchCapability

**Framework**: UIKit  
**Kind**: enum

Keys that indicate the availability of 3D Touch on a device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum UIForceTouchCapability
```

#### Overview

Only certain devices support 3D Touch. On those that do, the user can disable 3D Touch in the Accessibility area in Settings.

## Topics

### Availability options
- [UIForceTouchCapability.unknown](uiforcetouchcapability/unknown.md)
  The availability of 3D Touch is unknown.
- [UIForceTouchCapability.available](uiforcetouchcapability/available.md)
  3D Touch is available on the device.
- [UIForceTouchCapability.unavailable](uiforcetouchcapability/unavailable.md)
  3D Touch isn’t available on the device.
### Initializers
- [init?(rawValue: Int)](uiforcetouchcapability/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var forceTouchCapability: UIForceTouchCapability](uitraitcollection/forcetouchcapability.md)
  The force touch capability value of the trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiforcetouchcapability)*