# NSTextSelectionNavigation.Modifier

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Values that describe how the framework handles different kinds of selection modifiers.

**Availability**:
- macOS 12.0+

## Declaration

```swift
struct Modifier
```

```c
enum NSTextSelectionNavigationModifier : NSUInteger;
```

## Topics

### Creating a navigation modifier
- [init(rawValue: UInt)](./modifier/init%28rawvalue%29.md)
  Creates a new navigation modifier using a raw value.
### Navigation modifier characteristics
- [static var extend: NSTextSelectionNavigation.Modifier](./modifier/extend.md)
  The value that indicates the framework extends the selection by not moving the initial location while in a drag selection.
- [static var multiple: NSTextSelectionNavigation.Modifier](./modifier/multiple.md)
  The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and dragged positions.
- [static var visual: NSTextSelectionNavigation.Modifier](./modifier/visual.md)
  The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and drag positions.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Selection characteristics
- [var allowsNonContiguousRanges: Bool](./allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](./rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Destination](./destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](./direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](./textselection%28for,enclosing,incontainerat%29.md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/modifier)*