# textSelections(interactingAt:inContainerAt:anchors:modifiers:selecting:bounds:)

**Framework**: AppKit  
**Kind**: method

Returns an array of text selections produced by a tap or click at the point you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func textSelections(interactingAt point: CGPoint, inContainerAt containerLocation: any NSTextLocation, anchors: [NSTextSelection], modifiers: NSTextSelectionNavigation.Modifier, selecting: Bool, bounds: CGRect) -> [NSTextSelection]
```

#### Return Value

An array of text selections.

## Parameters

- `point`: A   that represents the location of the tap or click.
- `containerLocation`: A  .
- `anchors`: An array of   objects.
- `modifiers`: One or more   options.
- `selecting`: A Boolean value that indicates if the selection is in drag session.
- `bounds`: A   that defines the view area in the container’s coordinate system that can interact with events.

## See Also

- [func textSelection(for: NSTextSelection.Granularity, enclosing: NSTextSelection) -> NSTextSelection](nstextselectionnavigation/textselection(for:enclosing:).md)
  Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.
- [func destinationSelection(for: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, extending: Bool, confined: Bool) -> NSTextSelection?](nstextselectionnavigation/destinationselection(for:direction:destination:extending:confined:).md)
  Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/textselections(interactingat:incontainerat:anchors:modifiers:selecting:bounds:))*