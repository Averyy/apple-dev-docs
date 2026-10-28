# body1TextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The top line of body text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var body1TextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * body1TextProvider;
```

## Discussion

If you don’t specify a value for the [`body2TextProvider`](./body2textprovider.md) property, the text in this property wraps to the second line.

## See Also

### Setting the Complication Data
- [var headerImageProvider: CLKImageProvider?](./headerimageprovider.md)
  An optional image to display in the header.
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The text to display in the header line.
- [var body2TextProvider: CLKTextProvider?](./body2textprovider.md)
  An optional second line of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody/body1textprovider)*