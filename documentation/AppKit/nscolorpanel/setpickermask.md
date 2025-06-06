# setPickerMask(_:)

**Framework**: AppKit  
**Kind**: method

Determines which color selection modes are available in an application’s `NSColorPanel`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func setPickerMask(_ mask: NSColorPanel.Options)
```

#### Discussion

This method has an effect only before an `NSColorPanel` object is instantiated.

If you create a class that implements the color-picking protocols (`NSColorPickingDefault` and `NSColorPickingCustom`), you may want to give it a unique mask—one different from those defined for the standard color pickers. To display your color picker, your application will need to logically OR that unique mask with the standard color mask constants when invoking this method.

## Parameters

- `mask`: One or more logically ORed color mode masks described in  .

## See Also

- [class func setPickerMode(NSColorPanel.Mode)](nscolorpanel/setpickermode(_:).md)
  Specifies the color panel’s initial picker.
- [var mode: NSColorPanel.Mode](nscolorpanel/mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [NSColorPanel.Mode](nscolorpanel/mode-swift.enum.md)
  A type defined for the `enum` constants specifying color panel modes.
- [NSColorPanel.Options](nscolorpanel/options.md)
  The color modes that are enabled for a color panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/setpickermask(_:))*