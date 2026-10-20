# CLKSimpleGaugeProviderFillFractionEmpty

**Framework**: ClockKit  
**Kind**: var  
**Role**: Global Variable

A fill value indicating an empty gauge.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
let CLKSimpleGaugeProviderFillFractionEmpty: Float
```

```c
extern const float CLKSimpleGaugeProviderFillFractionEmpty;
```

#### Discussion

For [`CLKGaugeProviderStyle.ring`](./clkgaugeproviderstyle/ring.md) style gauges, the [`CLKSimpleGaugeProviderFillFractionEmpty`](./clksimplegaugeproviderfillfractionempty.md) value hides the ring, while setting a `0.0` fill value still shows the ring.

## See Also

### Gauge providers
- [class CLKSimpleGaugeProvider](./clksimplegaugeprovider.md)
  A gauge that shows a fractional value.
- [class CLKTimeIntervalGaugeProvider](./clktimeintervalgaugeprovider.md)
  A gauge that tracks time intervals.
- [class CLKGaugeProvider](./clkgaugeprovider.md)
  An abstract superclass that provides all the common behaviors for the gauge providers.
- [enum CLKGaugeProviderStyle](./clkgaugeproviderstyle.md)
  Visual styles available for gauges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimplegaugeproviderfillfractionempty)*