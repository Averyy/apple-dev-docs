# init(pickerMask:colorPanel:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes the color picker with the specified color panel and color picker mode mask.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
init?(pickerMask mask: Int, colorPanel owningColorPanel: NSColorPanel)
```

```objc
- (instancetype) initWithPickerMask:(NSUInteger) mask colorPanel:(NSColorPanel *) owningColorPanel;
```

#### Return Value

An initialized color picker object.

#### Discussion

Override this method to respond to the values in `mask` or do other custom initialization. If you override this method in a subclass, you should forward the message to `super` as part of the implementation.

## Parameters

- `mask`: The color picker mask.
- `owningColorPanel`: The `NSColorPanel` that owns the color picker. This value is cached so it can be accessed using the [`colorPanel`](./colorpanel.md) property.

## See Also

### Related Documentation
- [var colorPanel: NSColorPanel](./colorpanel.md)
  The color panel instance that owns the color picker.
- [init?(pickerMask: Int, colorPanel: NSColorPanel)](../nscolorpickingdefault/init%28pickermask,colorpanel%29.md)
  Initializes the receiver with a given color panel and its mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker/init(pickermask:colorpanel:))*