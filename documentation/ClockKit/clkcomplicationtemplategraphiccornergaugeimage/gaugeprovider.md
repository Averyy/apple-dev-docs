# gaugeProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The gauge to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var gaugeProvider: CLKGaugeProvider { get set }
```

```objc
@property (nonatomic, copy) CLKGaugeProvider * gaugeProvider;
```

## See Also

### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](./imageprovider.md)
  The image to display.
- [var leadingTextProvider: CLKTextProvider?](./leadingtextprovider.md)
  The text to display on the leading edge of the gauge.
- [var trailingTextProvider: CLKTextProvider?](./trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeimage/gaugeprovider)*