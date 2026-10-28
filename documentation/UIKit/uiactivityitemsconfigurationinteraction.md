# UIActivityItemsConfigurationInteraction

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * UIActivityItemsConfigurationInteraction;
```

## Overview

Specify which interactions you want the activity view to include in [`supportedInteractions`](./uiactivityitemsconfiguration/supportedinteractions.md).

## Topics

### Selecting interactions
- [static let copy: UIActivityItemsConfigurationInteraction](./uiactivityitemsconfigurationinteraction/copy.md)
  The copy interaction.
- [static let share: UIActivityItemsConfigurationInteraction](./uiactivityitemsconfigurationinteraction/share.md)
  The share interaction.
### Creating an interaction type
- [init(String)](./uiactivityitemsconfigurationinteraction/init%28_%29.md)
  Creates an activity items configuration interaction.
- [init(rawValue: String)](./uiactivityitemsconfigurationinteraction/init%28rawvalue%29.md)
  Creates an activity items configuration interaction with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing supported interactions
- [var supportedInteractions: [UIActivityItemsConfigurationInteraction]](./uiactivityitemsconfiguration/supportedinteractions.md)
  The types of interactions that the configuration supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationinteraction)*