# supportsMode(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether or not the receiver supports the specified picking mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func supportsMode(_ mode: NSColorPanel.Mode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the color picker supports the specified color picking mode; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is invoked when the `NSColorPanel` is first initialized: It is used to attempt to restore the user’s previously selected mode. It is also invoked by `NSColorPanel`‘s [`mode`](nscolorpanel/mode-swift.property.md) method to find the color picker that supports a particular mode. See this protocol description’s list of the unique mode values for the standard color pickers used by the Application Kit.

## Parameters

- `mode`: The color picking mode.

## See Also

- [func currentMode() -> NSColorPanel.Mode](nscolorpickingcustom/currentmode.md)
  Returns the receiver’s current mode (or submode, if applicable).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingcustom/supportsmode(_:))*