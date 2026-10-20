# supportsMode(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value indicating whether or not the receiver supports the specified picking mode.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func supportsMode(_ mode: NSColorPanel.Mode) -> Bool
```

```objc
- (BOOL) supportsMode:(NSColorPanelMode) mode;
```

#### Return Value

[`true`](../../Swift/true.md) if the color picker supports the specified color picking mode; otherwise [`false`](../../Swift/false.md).

#### Discussion

This method is invoked when the `NSColorPanel` is first initialized: It is used to attempt to restore the user’s previously selected mode. It is also invoked by `NSColorPanel`‘s [`mode`](../nscolorpanel/mode-swift.property.md) method to find the color picker that supports a particular mode. See this protocol description’s list of the unique mode values for the standard color pickers used by the Application Kit.

## Parameters

- `mode`: The color picking mode.

## See Also

### Getting Color Picker Information
- [func currentMode() -> NSColorPanel.Mode](./currentmode%28%29.md)
  Returns the receiver’s current mode (or submode, if applicable).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingcustom/supportsmode(_:))*