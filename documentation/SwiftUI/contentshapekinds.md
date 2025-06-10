# ContentShapeKinds

**Framework**: SwiftUI  
**Kind**: struct

A kind for the content shape of a view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct ContentShapeKinds
```

#### Overview

The kind is used by the system to influence various effects, hit-testing, and more.

## Topics

### Getting shape kinds
- [static let interaction: ContentShapeKinds](contentshapekinds/interaction.md)
  The kind for hit-testing and accessibility.
- [static let dragPreview: ContentShapeKinds](contentshapekinds/dragpreview.md)
  The kind for drag and drop previews.
- [static let contextMenuPreview: ContentShapeKinds](contentshapekinds/contextmenupreview.md)
  The kind for context menu previews.
- [static let focusEffect: ContentShapeKinds](contentshapekinds/focuseffect.md)
  The kind for the focus effect.
- [static let hoverEffect: ContentShapeKinds](contentshapekinds/hovereffect.md)
  The kind for hover effects.
- [static let accessibility: ContentShapeKinds](contentshapekinds/accessibility.md)
  The kind for accessibility visuals and sorting.
### Creating a set of options
- [init(rawValue: Int)](contentshapekinds/init(rawvalue:).md)
  Creates a content shape kind.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func allowsTightening(Bool) -> some View](view/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func contentShape<S>(S, eoFill: Bool) -> some View](view/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](view/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentshapekinds)*