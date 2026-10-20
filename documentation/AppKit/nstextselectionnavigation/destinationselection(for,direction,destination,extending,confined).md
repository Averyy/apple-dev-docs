# destinationSelection(for:direction:destination:extending:confined:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func destinationSelection(for textSelection: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, extending: Bool, confined: Bool) -> NSTextSelection?
```

```objc
- (NSTextSelection *) destinationSelectionForTextSelection:(NSTextSelection *) textSelection direction:(NSTextSelectionNavigationDirection) direction destination:(NSTextSelectionNavigationDestination) destination extending:(BOOL) extending confined:(BOOL) confined;
```

#### Return Value

A new [`NSTextSelection`](../nstextselection.md), or `nil` if the operation doesn’t produce a logically valid result.

#### Discussion

If `confined` is `true`, confine any movement to the text element that the selection already lies within.

## Parameters

- `textSelection`: The source selection.
- `direction`: One of the available [`NSTextSelectionNavigation.Direction`](./direction.md) directions.
- `destination`: One of the available [`NSTextSelectionNavigation.Destination`](./destination.md) destinations.
- `extending`: Whether this selection extends an existing selection.
- `confined`: Whether to confine movement to the existing selection.

## See Also

### Working with text selections
- [func textSelection(for: NSTextSelection.Granularity, enclosing: NSTextSelection) -> NSTextSelection](./textselection%28for,enclosing%29.md)
  Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.
- [func textSelections(interactingAt: CGPoint, inContainerAt: any NSTextLocation, anchors: [NSTextSelection], modifiers: NSTextSelectionNavigation.Modifier, selecting: Bool, bounds: CGRect) -> [NSTextSelection]](./textselections%28interactingat,incontainerat,anchors,modifiers,selecting,bounds%29.md)
  Returns an array of text selections produced by a tap or click at the point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/destinationselection(for:direction:destination:extending:confined:))*