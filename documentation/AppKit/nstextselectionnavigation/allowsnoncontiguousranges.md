# allowsNonContiguousRanges

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines if the instance could produce selections with multiple noncontiguous selections.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var allowsNonContiguousRanges: Bool { get set }
```

```objc
@property BOOL allowsNonContiguousRanges;
```

## See Also

### Selection characteristics
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](./rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](./modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](./destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](./direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](./textselection%28for,enclosing,incontainerat%29.md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/allowsnoncontiguousranges)*