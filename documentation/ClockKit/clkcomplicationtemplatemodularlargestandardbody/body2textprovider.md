# body2TextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

An optional second line of body text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var body2TextProvider: CLKTextProvider? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLKTextProvider * body2TextProvider;
```

#### Discussion

If you don’t specify a value for this property, the text in the [`body1TextProvider`](./body1textprovider.md) property wraps and is displayed on the second line.

## See Also

### Setting the Complication Data
- [var headerImageProvider: CLKImageProvider?](./headerimageprovider.md)
  An optional image to display in the header.
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The text to display in the header line.
- [var body1TextProvider: CLKTextProvider](./body1textprovider.md)
  The top line of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/body2textprovider)*