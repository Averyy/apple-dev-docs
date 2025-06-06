# valueAccessoryWidth

**Framework**: AppKit  
**Kind**: property

The width of the value accessories that appear at either end of the slider.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var valueAccessoryWidth: NSSliderAccessory.Width { get set }
```

#### Discussion

You can provide your own custom width, or use the system-provided [`default`](nsslideraccessory/width/default.md) or [`wide`](nsslideraccessory/width/wide.md) options.

The default value is [`default`](nsslideraccessory/width/default.md).

## See Also

- [var minimumValueAccessory: NSSliderAccessory?](nsslidertouchbaritem/minimumvalueaccessory.md)
  The accessory that appears at the end of the slider with the minimum value.
- [var maximumValueAccessory: NSSliderAccessory?](nsslidertouchbaritem/maximumvalueaccessory.md)
  The accessory that appears at the end of the slider with the maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidertouchbaritem/valueaccessorywidth)*