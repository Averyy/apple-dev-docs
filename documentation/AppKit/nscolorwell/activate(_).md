# activate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Activates the color well, displays the color panel, and synchronizes the two UI elements.

**Availability**:
- macOS

## Declaration

```swift
func activate(_ exclusive: Bool)
```

```objc
- (void) activate:(BOOL) exclusive;
```

## Discussion

When you call this method, the color well displays the standard color panel and sets the panel’s current color to the value in the color well. When someone changes the color in the color panel, the color well updates its selected color to match. If the color well’s [`isBordered`](./isbordered.md) property is [`true`](../../Swift/true.md), the color well highlights that border while it’s active.

## Parameters

- `exclusive`: [`true`](../../Swift/true.md) to deactivate any other color wells; [`false`](../../Swift/false.md) to keep them active. If a color panel is active with `exclusive` set to [`true`](../../Swift/true.md) and another is subsequently activated with `exclusive` set to [`false`](../../Swift/false.md), the exclusive setting of the first panel is ignored.

## See Also

### Activating and deactivating color wells
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the color well is currently active.
- [func deactivate()](./deactivate%28%29.md)
  Deactivates the color well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/activate(_:))*