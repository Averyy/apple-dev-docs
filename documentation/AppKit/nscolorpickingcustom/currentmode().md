# currentMode()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the receiver’s current mode (or submode, if applicable).

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func currentMode() -> NSColorPanel.Mode
```

```objc
- (NSColorPanelMode) currentMode;
```

## Return Value

The current color picker mode. The returned value should be unique to your color picker. See this protocol description’s list of the unique values for the standard color pickers used by the Application Kit.

## See Also

### Getting Color Picker Information
- [func supportsMode(NSColorPanel.Mode) -> Bool](./supportsmode%28_%29.md)
  Returns a Boolean value indicating whether or not the receiver supports the specified picking mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingcustom/currentmode())*