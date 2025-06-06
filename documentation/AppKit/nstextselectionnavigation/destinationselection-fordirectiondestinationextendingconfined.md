# destinationSelection(for:direction:destination:extending:confined:)

**Framework**: AppKit  
**Kind**: method

Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func destinationSelection(for textSelection: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, extending: Bool, confined: Bool) -> NSTextSelection?
```

#### Return Value

A new [`NSTextSelection`](nstextselection.md), or `nil` if the operation doesn’t produce a logically valid result.

#### Discussion

If `confined` is `true`, confine any movement to the text element that the selection already lies within.

## Parameters

- `textSelection`: The source selection.
- `direction`: One of the available   directions.
- `destination`: One of the available   destinations.
- `extending`: Whether this selection extends an existing selection.
- `confined`: Whether to confine movement to the existing selection.

## See Also

- [func textSelection(for: NSTextSelection.Granularity, enclosing: NSTextSelection) -> NSTextSelection](nstextselectionnavigation/textselection(for:enclosing:).md)
  Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.
- [func textSelections(interactingAt: CGPoint, inContainerAt: any NSTextLocation, anchors: [NSTextSelection], modifiers: NSTextSelectionNavigation.Modifier, selecting: Bool, bounds: CGRect) -> [NSTextSelection]](nstextselectionnavigation/textselections(interactingat:incontainerat:anchors:modifiers:selecting:bounds:).md)
  Returns an array of text selections produced by a tap or click at the point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/destinationselection(for:direction:destination:extending:confined:))*