# textSelection(for:enclosing:inContainerAt:)

**Framework**: UIKit  
**Kind**: method

Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textSelection(for selectionGranularity: NSTextSelection.Granularity, enclosing point: CGPoint, inContainerAt location: any NSTextLocation) -> NSTextSelection?
```

#### Return Value

A new `NSTextSelection`, or `nil` if the text selection is not found.

## Parameters

- `selectionGranularity`: One of the available   options.
- `point`: The point that encloses the text.
- `location`: An   that describes the container.

## See Also

- [var allowsNonContiguousRanges: Bool](nstextselectionnavigation/allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](nstextselectionnavigation/destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](nstextselectionnavigation/direction.md)
  Values that describe the direction of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/textselection(for:enclosing:incontainerat:))*