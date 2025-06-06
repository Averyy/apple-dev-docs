# rotatesCoordinateSystemForLayoutOrientation

**Framework**: UIKit  
**Kind**: property

Determines if the framework rotates the coordinate system to match the layout orientation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var rotatesCoordinateSystemForLayoutOrientation: Bool { get set }
```

#### Discussion

If set to `true`, the framework rotates the coordinate system for arguments passed to the navigation methods such as [`textSelections(interactingAt:inContainerAt:anchors:modifiers:selecting:bounds:)`](nstextselectionnavigation/textselections(interactingat:incontainerat:anchors:modifiers:selecting:bounds:).md): based on the text container layout orientation. Defaults to `false`.

## See Also

- [var allowsNonContiguousRanges: Bool](nstextselectionnavigation/allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](nstextselectionnavigation/destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](nstextselectionnavigation/direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](nstextselectionnavigation/textselection(for:enclosing:incontainerat:).md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation)*