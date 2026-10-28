# LegibilityWeight

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

The Accessibility Bold Text user setting options.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum LegibilityWeight
```

## Overview

The app can’t override the user’s choice before iOS 16, tvOS 16 or watchOS 9.0.

## Topics

### Getting weights
- [LegibilityWeight.regular](./legibilityweight/regular.md)
  Use regular font weight (no Accessibility Bold).
- [LegibilityWeight.bold](./legibilityweight/bold.md)
  Use heavier font weight (force Accessibility Bold).
### Creating a weight
- [init?(UILegibilityWeight)](./legibilityweight/init%28_%29.md)
  Creates a legibility weight from its UILegibilityWeight equivalent.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Improving legibility
- [var accessibilityReduceTransparency: Bool](./environmentvalues/accessibilityreducetransparency.md)
  Whether the system preference for Reduce Transparency is enabled.
- [var legibilityWeight: LegibilityWeight?](./environmentvalues/legibilityweight.md)
  The font weight to apply to text.
- [var accessibilityShowButtonShapes: Bool](./environmentvalues/accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/legibilityweight)*