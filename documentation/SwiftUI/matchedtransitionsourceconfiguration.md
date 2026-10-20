# MatchedTransitionSourceConfiguration

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

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
- [func background(Color) -> some MatchedTransitionSourceConfiguration](./matchedtransitionsourceconfiguration/background%28_%29.md)
  Specifies a color that will be drawn behind the content within the matched transition source.
- [func clipShape(RoundedRectangle) -> some MatchedTransitionSourceConfiguration](./matchedtransitionsourceconfiguration/clipshape%28_%29.md)
  Applies the specified shape as to the matched transition source, clipping its content.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some MatchedTransitionSourceConfiguration](./matchedtransitionsourceconfiguration/shadow%28color,radius,x,y%29.md)
  Applies the specified shadow effect to the matched transition source.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [EmptyMatchedTransitionSourceConfiguration](./emptymatchedtransitionsourceconfiguration.md)

## See Also

### Defining matched transitions
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](./view/matchedtransitionsource%28id,in%29.md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](./view/matchedtransitionsource%28id,in,configuration%29.md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [struct EmptyMatchedTransitionSourceConfiguration](./emptymatchedtransitionsourceconfiguration.md)
  An unstyled matched transition source configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/matchedtransitionsourceconfiguration)*