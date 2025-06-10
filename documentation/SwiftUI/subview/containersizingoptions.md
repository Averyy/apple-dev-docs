# Subview.ContainerSizingOptions

**Framework**: SwiftUI  
**Kind**: enum

Options on how all subviews should be sized when in a container.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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