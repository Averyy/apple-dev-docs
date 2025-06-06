# customizationPaletteIsRunning

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar’s customization palette is in use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var customizationPaletteIsRunning: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the toolbar’s customization palette is running; otherwise, it’s [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func runCustomizationPalette(Any?)](nstoolbar/runcustomizationpalette(_:).md)
  Displays the toolbar’s customization palette and handles any user-initiated customizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/customizationpaletteisrunning)*