# Subview.ContainerSizingOptions

**Framework**: SwiftUI  
**Kind**: enum

Options on how all subviews should be sized when in a container.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum ContainerSizingOptions
```

#### Overview

> **Note**: This option is not about the sizing considerations of a view being measured individually. Instead, this option describes the sizing characteristics of a group of subviews altogether, which also would only have actual effects when used in a container.

## Topics

### Enumeration Cases
- [Subview.ContainerSizingOptions.uniform(axis:)](subview/containersizingoptions/uniform(axis:).md)
  Subviews will share the same size.
- [Subview.ContainerSizingOptions.variable](subview/containersizingoptions/variable.md)
  Subviews will be sized individually.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/subview/containersizingoptions)*