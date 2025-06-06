# runCustomizationPalette(_:)

**Framework**: AppKit  
**Kind**: method

Displays the toolbar’s customization palette and handles any user-initiated customizations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
func runCustomizationPalette(_ sender: Any?)
```

#### Discussion

While the customization palette is visible, the toolbar calls methods of its delegate to manage configuration changes.

## Parameters

- `sender`: The control sending the message.

## See Also

- [var customizationPaletteIsRunning: Bool](nstoolbar/customizationpaletteisrunning.md)
  A Boolean value that indicates whether the toolbar’s customization palette is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/runcustomizationpalette(_:))*