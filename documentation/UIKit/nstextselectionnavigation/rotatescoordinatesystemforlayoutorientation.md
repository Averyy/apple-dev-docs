# rotatesCoordinateSystemForLayoutOrientation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL rotatesCoordinateSystemForLayoutOrientation;
```

## Discussion

If set to `true`, the framework rotates the coordinate system for arguments passed to the navigation methods such as [`textSelections(interactingAt:inContainerAt:anchors:modifiers:selecting:bounds:)`](./textselections%28interactingat,incontainerat,anchors,modifiers,selecting,bounds%29.md): based on the text container layout orientation. Defaults to `false`.

## See Also

### Selection characteristics
- [var allowsNonContiguousRanges: Bool](./allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [NSTextSelectionNavigation.Modifier](./modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](./destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [NSTextSelectionNavigation.Direction](./direction.md)
  Values that describe the direction of a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](./textselection%28for,enclosing,incontainerat%29.md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation)*