# textSelection(for:enclosing:)

**Framework**: UIKit  
**Kind**: method

Returns a text selection expanded to the nearest boundaries for the selection granularity and enclosing text selection text ranges you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textSelection(for selectionGranularity: NSTextSelection.Granularity, enclosing textSelection: NSTextSelection) -> NSTextSelection
```

#### Return Value

A new text selection.

## Parameters

- `selectionGranularity`: One of the available   options.
- `textSelection`: The text selection that describes the text range of interest.

## See Also

- [func textSelections(interactingAt: CGPoint, inContainerAt: any NSTextLocation, anchors: [NSTextSelection], modifiers: NSTextSelectionNavigation.Modifier, selecting: Bool, bounds: CGRect) -> [NSTextSelection]](nstextselectionnavigation/textselections(interactingat:incontainerat:anchors:modifiers:selecting:bounds:).md)
  Returns an array of text selections produced by a tap or click at the point you specify.
- [func destinationSelection(for: NSTextSelection, direction: NSTextSelectionNavigation.Direction, destination: NSTextSelectionNavigation.Destination, extending: Bool, confined: Bool) -> NSTextSelection?](nstextselectionnavigation/destinationselection(for:direction:destination:extending:confined:).md)
  Returns a new selection that results from applying the navigation operations you specify to the text selection you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/textselection(for:enclosing:))*