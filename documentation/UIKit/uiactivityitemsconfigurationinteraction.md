# UIActivityItemsConfigurationInteraction

**Framework**: UIKit  
**Kind**: struct

A structure that describes types of interactions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct UIActivityItemsConfigurationInteraction
```

#### Overview

Specify which interactions you want the activity view to include in [`supportedInteractions`](uiactivityitemsconfiguration/supportedinteractions.md).

## Topics

### Selecting interactions
- [static let copy: UIActivityItemsConfigurationInteraction](uiactivityitemsconfigurationinteraction/copy.md)
  The copy interaction.
- [static let share: UIActivityItemsConfigurationInteraction](uiactivityitemsconfigurationinteraction/share.md)
  The share interaction.
### Creating an interaction type
- [init(String)](uiactivityitemsconfigurationinteraction/init(_:).md)
  Creates an activity items configuration interaction.
- [init(rawValue: String)](uiactivityitemsconfigurationinteraction/init(rawvalue:).md)
  Creates an activity items configuration interaction with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var supportedInteractions: [UIActivityItemsConfigurationInteraction]](uiactivityitemsconfiguration/supportedinteractions.md)
  The types of interactions that the configuration supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationinteraction)*