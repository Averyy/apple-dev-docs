# MatchedTransitionSourceConfiguration

**Framework**: SwiftUI  
**Kind**: protocol

A configuration that defines the appearance of a matched transition source.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol MatchedTransitionSourceConfiguration : Sendable
```

## Topics

### Instance Methods
- [func background(Color) -> some MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration/background(_:).md)
  Specifies a color that will be drawn behind the content within the matched transition source.
- [func clipShape(RoundedRectangle) -> some MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration/clipshape(_:).md)
  Applies the specified shape as to the matched transition source, clipping its content.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration/shadow(color:radius:x:y:).md)
  Applies the specified shadow effect to the matched transition source.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [EmptyMatchedTransitionSourceConfiguration](emptymatchedtransitionsourceconfiguration.md)

## See Also

- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](view/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](view/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [struct EmptyMatchedTransitionSourceConfiguration](emptymatchedtransitionsourceconfiguration.md)
  An unstyled matched transition source configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/matchedtransitionsourceconfiguration)*