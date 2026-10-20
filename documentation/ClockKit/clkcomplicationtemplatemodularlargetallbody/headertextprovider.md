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

A tint color is applied to the header text to differentiate it from the other rows. In multicolor environments, the text provider or template provide the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

### Setting the Complication Data
- [var bodyTextProvider: CLKTextProvider](./bodytextprovider.md)
  The text to display in the body line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetallbody/headertextprovider)*