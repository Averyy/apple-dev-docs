# activate(_:)

**Framework**: AppKit  
**Kind**: method

Activates the color well, displays the color panel, and synchronizes the two UI elements.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func activate(_ exclusive: Bool)
```

#### Discussion

When you call this method, the color well displays the standard color panel and sets the panel’s current color to the value in the color well. When someone changes the color in the color panel, the color well updates its selected color to match. If the color well’s [`isBordered`](nscolorwell/isbordered.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), the color well highlights that border while it’s active.

## Parameters

- `exclusive`:   to deactivate any other color wells;   to keep them active. If a color panel is active with   set to   and another is subsequently activated with   set to  , the exclusive setting of the first panel is ignored.

## See Also

- [var isActive: Bool](nscolorwell/isactive.md)
  A Boolean value that indicates whether the color well is currently active.
- [func deactivate()](nscolorwell/deactivate.md)
  Deactivates the color well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/activate(_:))*