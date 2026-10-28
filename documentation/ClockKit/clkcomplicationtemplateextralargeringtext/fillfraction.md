# fillFraction

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

Setting the Complication Data.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var fillFraction: Float { get set }
```

```objc
@property (nonatomic) float fillFraction;
```

## Discussion

Specify a value between `0.0` and `1.0`, where `0.0` represents no ring and `1.0` represents a complete ring.

## See Also

### Setting the Complication Data
- [var ringStyle: CLKComplicationRingStyle](./ringstyle.md)
  The style of the progress ring.
- [var textProvider: CLKTextProvider](./textprovider.md)
  The text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/fillfraction)*