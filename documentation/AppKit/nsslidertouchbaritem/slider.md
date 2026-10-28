# slider

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The slider displayed by the bar item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var slider: NSSlider { get set }
```

```objc
@property (strong) NSSlider * slider;
```

## Discussion

The slider is automatically created by the item, but you can provide a custom subclass to this property to customize behavior.

## See Also

### Configuring the slider
- [var label: String?](./label.md)
  The text displayed alongside the slider.
- [var view: any NSView & NSUserInterfaceCompression](./view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidertouchbaritem/slider)*