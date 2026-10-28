# valueAccessoryWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The width of the value accessories that appear at either end of the slider.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var valueAccessoryWidth: NSSliderAccessory.Width { get set }
```

```objc
@property NSSliderAccessoryWidth valueAccessoryWidth;
```

## Discussion

You can provide your own custom width, or use the system-provided [`default`](../nsslideraccessory/width/default.md) or [`wide`](../nsslideraccessory/width/wide.md) options.

The default value is [`default`](../nsslideraccessory/width/default.md).

## See Also

### Configuring slider accessories
- [var minimumValueAccessory: NSSliderAccessory?](./minimumvalueaccessory.md)
  The accessory that appears at the end of the slider with the minimum value.
- [var maximumValueAccessory: NSSliderAccessory?](./maximumvalueaccessory.md)
  The accessory that appears at the end of the slider with the maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidertouchbaritem/valueaccessorywidth)*