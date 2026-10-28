# fillFraction

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The fraction of the ring to fill.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

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
- [var textProvider: CLKTextProvider](./textprovider.md)
  The text to display in the complication.
- [var ringStyle: CLKComplicationRingStyle](./ringstyle.md)
  The style of the progress ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringtext/fillfraction)*