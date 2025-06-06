# accessibilityIgnoresInvertColors(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets whether this view should ignore the system Smart Invert setting.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityIgnoresInvertColors(_ active: Bool = true) -> some View
```

#### Discussion

Use this modifier to suppress Smart Invert in a view that shouldn’t be inverted. Or pass an `active` argument of `false` to begin following the Smart Invert setting again when it was previously disabled.

## Parameters

- `active`: A true value ignores the system Smart Invert   setting. A false value follows the system setting.

## See Also

- [var accessibilityInvertColors: Bool](environmentvalues/accessibilityinvertcolors.md)
  Whether the system preference for Invert Colors is enabled.
- [var accessibilityDifferentiateWithoutColor: Bool](environmentvalues/accessibilitydifferentiatewithoutcolor.md)
  Whether the system preference for Differentiate without Color is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityignoresinvertcolors(_:))*