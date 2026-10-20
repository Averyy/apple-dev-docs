# headerImageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

An optional image to display in the header.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var headerImageProvider: CLKImageProvider? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLKImageProvider * headerImageProvider;
```

#### Discussion

A tint color is applied to the header image to differentiate it from the other rows. In multicolor environments, the image provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The text to display in the header line.
- [var body1TextProvider: CLKTextProvider](./body1textprovider.md)
  The top line of body text.
- [var body2TextProvider: CLKTextProvider?](./body2textprovider.md)
  An optional second line of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/headerimageprovider)*