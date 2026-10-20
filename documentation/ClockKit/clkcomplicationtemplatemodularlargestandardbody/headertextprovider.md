# headerTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display in the header line.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var headerTextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * headerTextProvider;
```

#### Discussion

The width of the header image determines how much space is available for displaying text. A tint color is applied to the header text to differentiate it from the body text rows. In multicolor environments, the text provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

### Setting the Complication Data
- [var headerImageProvider: CLKImageProvider?](./headerimageprovider.md)
  An optional image to display in the header.
- [var body1TextProvider: CLKTextProvider](./body1textprovider.md)
  The top line of body text.
- [var body2TextProvider: CLKTextProvider?](./body2textprovider.md)
  An optional second line of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/headertextprovider)*