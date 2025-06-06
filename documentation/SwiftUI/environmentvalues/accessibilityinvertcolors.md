# accessibilityInvertColors

**Framework**: SwiftUI  
**Kind**: property

Whether the system preference for Invert Colors is enabled.

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
var accessibilityInvertColors: Bool { get }
```

#### Discussion

If this property’s value is true then the display will be inverted. In these cases it may be needed for UI drawing to be adjusted to in order to display optimally when inverted.

## See Also

- [func accessibilityIgnoresInvertColors(Bool) -> some View](view/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
- [var accessibilityDifferentiateWithoutColor: Bool](environmentvalues/accessibilitydifferentiatewithoutcolor.md)
  Whether the system preference for Differentiate without Color is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityinvertcolors)*