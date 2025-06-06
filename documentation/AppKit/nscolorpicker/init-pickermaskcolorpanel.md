# init(pickerMask:colorPanel:)

**Framework**: AppKit  
**Kind**: init

Initializes the color picker with the specified color panel and color picker mode mask.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init?(pickerMask mask: Int, colorPanel owningColorPanel: NSColorPanel)
```

#### Return Value

An initialized color picker object.

#### Discussion

Override this method to respond to the values in `mask` or do other custom initialization. If you override this method in a subclass, you should forward the message to `super` as part of the implementation.

## Parameters

- `mask`: The color picker mask.
- `owningColorPanel`: The   that owns the color picker. This value is cached so it can be accessed using the   property.

## See Also

- [var colorPanel: NSColorPanel](nscolorpicker/colorpanel.md)
  The color panel instance that owns the color picker.
- [Color Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html#//apple_ref/doc/uid/10000082i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker/init(pickermask:colorpanel:))*