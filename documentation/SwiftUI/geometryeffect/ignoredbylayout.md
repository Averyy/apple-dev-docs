# ignoredByLayout()

**Framework**: SwiftUI  
**Kind**: method

Returns an effect that produces the same geometry transform as this effect, but only applies the transform while rendering its view.

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
func ignoredByLayout() -> _IgnoredByLayoutEffect<Self>
```

#### Discussion

Use this method to disable layout changes during transitions. The view ignores the transform returned by this method while the view is performing its layout calculations.

## See Also

- [func effectValue(size: CGSize) -> ProjectionTransform](geometryeffect/effectvalue(size:).md)
  Returns the current value of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryeffect/ignoredbylayout())*