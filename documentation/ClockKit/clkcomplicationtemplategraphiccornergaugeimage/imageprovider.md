# imageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The image to display.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var imageProvider: CLKFullColorImageProvider { get set }
```

```objc
@property (nonatomic, copy) CLKFullColorImageProvider * imageProvider;
```

## Discussion

This image provider produces a full-color image, masked to a circle.

## See Also

### Setting the Complication Data
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](./leadingtextprovider.md)
  The text to display on the leading edge of the gauge.
- [var trailingTextProvider: CLKTextProvider?](./trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeimage/imageprovider)*