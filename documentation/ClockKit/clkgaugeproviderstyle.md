# CLKGaugeProviderStyle

**Framework**: ClockKit  
**Kind**: enum  
**Role**: Enumeration

Visual styles available for gauges.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
enum CLKGaugeProviderStyle
```

```c
enum CLKGaugeProviderStyle : NSInteger;
```

## Topics

### Styles
- [CLKGaugeProviderStyle.fill](./clkgaugeproviderstyle/fill.md)
  A gauge that fills in as the value increases.
- [CLKGaugeProviderStyle.ring](./clkgaugeproviderstyle/ring.md)
  A gauge that indicates a value with a sliding ring.
### Initializers
- [init?(rawValue: Int)](./clkgaugeproviderstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Gauge providers
- [class CLKSimpleGaugeProvider](./clksimplegaugeprovider.md)
  A gauge that shows a fractional value.
- [class CLKTimeIntervalGaugeProvider](./clktimeintervalgaugeprovider.md)
  A gauge that tracks time intervals.
- [class CLKGaugeProvider](./clkgaugeprovider.md)
  An abstract superclass that provides all the common behaviors for the gauge providers.
- [let CLKSimpleGaugeProviderFillFractionEmpty: Float](./clksimplegaugeproviderfillfractionempty.md)
  A fill value indicating an empty gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkgaugeproviderstyle)*