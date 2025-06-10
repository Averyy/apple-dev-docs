# NSTextSelectionNavigation.Modifier

**Framework**: UIKit  
**Kind**: struct

Values that describe how the framework handles different kinds of selection modifiers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Modifier
```

## Topics

### Creating a navigation modifier
- [init(rawValue: UInt)](nstextselectionnavigation/modifier/init(rawvalue:).md)
  Creates a new navigation modifier using a raw value.
### Navigation modifier characteristics
- [static var extend: NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier/extend.md)
  The value that indicates the framework extends the selection by not moving the initial location while in a drag selection.
- [static var multiple: NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier/multiple.md)
  The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and dragged positions.
- [static var visual: NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier/visual.md)
  The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and drag positions.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var allowsNonContiguousRanges: Bool](nstextselectionnavigation/allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Destination](nstextselectionnavigation/destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](nstextselectionnavigation/direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](nstextselectionnavigation/textselection(for:enclosing:incontainerat:).md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/modifier)*