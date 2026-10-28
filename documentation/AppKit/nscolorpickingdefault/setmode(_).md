# setMode(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Specifies the receiver’s mode.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func setMode(_ mode: NSColorPanel.Mode)
```

```objc
- (void) setMode:(NSColorPanelMode) mode;
```

## Discussion

This method is invoked by the `NSColorPanel` method [`mode`](../nscolorpanel/mode-swift.property.md) method to ensure the color picker reflects the current mode. For example, invoke this method during color picker initialization to ensure that all color pickers are restored to the mode the user left them in the last time an `NSColorPanel` was used.

Most color pickers have only one mode and thus don’t need to do any work in this method. An example of a color picker that uses this method is the slider picker, which can choose from one of several submodes depending on the value of `mode`.

## Parameters

- `mode`: The color picker mode. The available modes are described in [Choosing the Color Pickers in a Color Panel](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/ChoosingColorPickers.html#//apple_ref/doc/uid/20000792).

## See Also

### Configuring Color Pickers
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](./insertnewbuttonimage%28_,in%29.md)
  Sets the image of a given button cell.
- [func provideNewButtonImage() -> NSImage](./providenewbuttonimage%28%29.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func minContentSize() -> NSSize](./mincontentsize%28%29.md)
  Indicates the receiver’s minimum content size.
- [func buttonToolTip() -> String](./buttontooltip%28%29.md)
  Provides the toolbar button help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/setmode(_:))*