# accessibilityShowButtonShapes

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

Whether the system preference for Show Button Shapes is enabled.

**Availability**:
- iOS 14.0+ - Deprecated in 1000.0 (renamed: accessibilityShowBorders)
- iPadOS 14.0+ - Deprecated in 1000.0 (renamed: accessibilityShowBorders)
- Mac Catalyst 14.0+ - Deprecated in 1000.0 (renamed: accessibilityShowBorders)
- macOS 11.0+ - Deprecated in 1000.0 (renamed: accessibilityShowBorders)
- tvOS 14.0+ - Deprecated in 1000.0 (renamed: accessibilityShowBorders)
- visionOS 1.0+ - Deprecated in 1000.0 (renamed: accessibilityShowBorders)
- watchOS 7.0+ - Deprecated in 1000.0 (renamed: accessibilityShowBorders)

## Declaration

```swift
var accessibilityShowButtonShapes: Bool { get }
```

#### Discussion

If this property’s value is true, interactive custom controls such as buttons should be drawn in such a way that their edges and borders are clearly visible.

## See Also

### Improving legibility
- [var accessibilityReduceTransparency: Bool](./accessibilityreducetransparency.md)
  Whether the system preference for Reduce Transparency is enabled.
- [var legibilityWeight: LegibilityWeight?](./legibilityweight.md)
  The font weight to apply to text.
- [enum LegibilityWeight](../legibilityweight.md)
  The Accessibility Bold Text user setting options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityshowbuttonshapes)*