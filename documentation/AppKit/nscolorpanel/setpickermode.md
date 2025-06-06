# setPickerMode(_:)

**Framework**: AppKit  
**Kind**: method

Specifies the color panel’s initial picker.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func setPickerMode(_ mode: NSColorPanel.Mode)
```

#### Discussion

This method may be called at any time, whether or not an application’s `NSColorPanel` has been instantiated.

## Parameters

- `mode`: A constant specifying which color picker mode is initially visible. This is one of the symbolic constants described in  .

## See Also

- [var mode: NSColorPanel.Mode](nscolorpanel/mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [NSColorPanel.Mode](nscolorpanel/mode-swift.enum.md)
  A type defined for the `enum` constants specifying color panel modes.
- [class func setPickerMask(NSColorPanel.Options)](nscolorpanel/setpickermask(_:).md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.
- [NSColorPanel.Options](nscolorpanel/options.md)
  The color modes that are enabled for a color panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/setpickermode(_:))*