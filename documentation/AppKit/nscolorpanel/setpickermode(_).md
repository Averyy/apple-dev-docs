# setPickerMode(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Specifies the color panel’s initial picker.

**Availability**:
- macOS

## Declaration

```swift
class func setPickerMode(_ mode: NSColorPanel.Mode)
```

```objc
+ (void) setPickerMode:(NSColorPanelMode) mode;
```

#### Discussion

This method may be called at any time, whether or not an application’s `NSColorPanel` has been instantiated.

## Parameters

- `mode`: A constant specifying which color picker mode is initially visible. This is one of the symbolic constants described in `Color Panel Modes`.

## See Also

### Setting color picker modes
- [var mode: NSColorPanel.Mode](./mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [NSColorPanel.Mode](./mode-swift.enum.md)
  A type defined for the `enum` constants specifying color panel modes.
- [class func setPickerMask(NSColorPanel.Options)](./setpickermask%28_%29.md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.
- [NSColorPanel.Options](./options.md)
  The color modes that are enabled for a color panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/setpickermode(_:))*