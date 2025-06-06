# init(pickerMask:colorPanel:)

**Framework**: AppKit  
**Kind**: init  
**Required**: Yes

Initializes the receiver with a given color panel and its mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init?(pickerMask mask: Int, colorPanel owningColorPanel: NSColorPanel)
```

#### Return Value

If your color picker responds to any of the modes represented in `panelModes`, it should perform its initialization and return an initialized color picker. Color pickers that do so have their buttons inserted in the color panel and continue to receive messages from the panel as the user manipulates it. If the color picker doesn’t respond to any of the modes represented in `panelModes`, it should do nothing and return `nil`.

#### Discussion

This method is sent by the `NSColorPanel` to all implementors of the color-picking protocols when the application’s color panel is first initialized. In order for your color picker to receive this message, it must have a bundle in your application’s “ColorPickers” directory (described in [`Adding Custom Color Pickers to a Color Panel`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/AddingColorPickers.html#//apple_ref/doc/uid/20000793)).

This method should examine the mask and determine whether it supports any of the modes included there. You may also check the value in `mask` to enable or disable any subpickers or optional controls implemented by your color picker. Your color picker may also retain `owningColorPanel` in an instance variable for future communication with the color panel.

This method is provided to initialize your color picker; however, much of a color picker’s initialization may be done lazily through the `NSColorPickingCustom` protocol’s [`provideNewView(_:)`](nscolorpickingcustom/providenewview(_:).md) method.

## Parameters

- `mask`: A mask indicating the various color picker modes supported by the color panel. This is determined by the argument to the   method  . If it has not been set,   is  . If your color picker supports any additional modes, you should invoke the   method when your application initializes to notify the   class. The standard mode constants are defined in  .
- `owningColorPanel`: The color panel than owns the receiver.

## See Also

- [Color Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html#//apple_ref/doc/uid/10000082i)
- [class func setPickerMask(NSColorPanel.Options)](nscolorpanel/setpickermask(_:).md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/init(pickermask:colorpanel:))*