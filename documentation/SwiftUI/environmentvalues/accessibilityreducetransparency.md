# accessibilityReduceTransparency

**Framework**: SwiftUI  
**Kind**: property

Whether the system preference for Reduce Transparency is enabled.

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
var accessibilityReduceTransparency: Bool { get }
```

#### Discussion

If this property’s value is true, UI (mainly window) backgrounds should not be semi-transparent; they should be opaque.

## See Also

- [var accessibilityShowButtonShapes: Bool](environmentvalues/accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.
- [var legibilityWeight: LegibilityWeight?](environmentvalues/legibilityweight.md)
  The font weight to apply to text.
- [enum LegibilityWeight](legibilityweight.md)
  The Accessibility Bold Text user setting options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducetransparency)*