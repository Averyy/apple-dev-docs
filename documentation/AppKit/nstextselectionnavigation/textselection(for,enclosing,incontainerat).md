# textSelection(for:enclosing:inContainerAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func textSelection(for selectionGranularity: NSTextSelection.Granularity, enclosing point: CGPoint, inContainerAt location: any NSTextLocation) -> NSTextSelection?
```

```objc
- (NSTextSelection *) textSelectionForSelectionGranularity:(NSTextSelectionGranularity) selectionGranularity enclosingPoint:(CGPoint) point inContainerAtLocation:(id<NSTextLocation>) location;
```

#### Return Value

A new `NSTextSelection`, or `nil` if the text selection is not found.

## Parameters

- `selectionGranularity`: One of the available [`NSTextSelection.Granularity`](../nstextselection/granularity-swift.enum.md) options.
- `point`: The point that encloses the text.
- `location`: An [`NSTextLocation`](../nstextlocation.md) that describes the container.

## See Also

### Selection characteristics
- [var allowsNonContiguousRanges: Bool](./allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](./rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](./modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](./destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](./direction.md)
  Values that describe the direction of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/textselection(for:enclosing:incontainerat:))*