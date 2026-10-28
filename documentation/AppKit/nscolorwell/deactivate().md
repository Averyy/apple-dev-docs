# deactivate()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deactivates the color well.

**Availability**:
- macOS

## Declaration

```swift
func deactivate()
```

```objc
- (void) deactivate;
```

## Discussion

This method detaches the color well from the system color panel. Future selections in the color panel don’t update the color well’s current color.

## See Also

### Activating and deactivating color wells
- [func activate(Bool)](./activate%28_%29.md)
  Activates the color well, displays the color panel, and synchronizes the two UI elements.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the color well is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/deactivate())*