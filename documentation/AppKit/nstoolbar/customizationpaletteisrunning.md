# customizationPaletteIsRunning

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar’s customization palette is in use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var customizationPaletteIsRunning: Bool { get }
```

```objc
@property (readonly) BOOL customizationPaletteIsRunning;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the toolbar’s customization palette is running; otherwise, it’s [`false`](../../Swift/false.md).

## See Also

### Displaying the customization palette
- [func runCustomizationPalette(Any?)](./runcustomizationpalette%28_%29.md)
  Displays the toolbar’s customization palette and handles any user-initiated customizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/customizationpaletteisrunning)*