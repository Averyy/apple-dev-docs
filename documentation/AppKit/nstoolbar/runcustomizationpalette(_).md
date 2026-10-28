# runCustomizationPalette(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the toolbar’s customization palette and handles any user-initiated customizations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
func runCustomizationPalette(_ sender: Any?)
```

```objc
- (void) runCustomizationPalette:(id) sender;
```

## Discussion

While the customization palette is visible, the toolbar calls methods of its delegate to manage configuration changes.

## Parameters

- `sender`: The control sending the message.

## See Also

### Displaying the customization palette
- [var customizationPaletteIsRunning: Bool](./customizationpaletteisrunning.md)
  A Boolean value that indicates whether the toolbar’s customization palette is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/runcustomizationpalette(_:))*