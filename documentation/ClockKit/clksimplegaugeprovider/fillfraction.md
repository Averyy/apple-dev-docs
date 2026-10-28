# fillFraction

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The value displayed by the gauge.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var fillFraction: Float { get }
```

```objc
@property (nonatomic, assign, readonly) float fillFraction;
```

## Discussion

Contains a value between `0.0` and `1.0`, or `CLKSimpleGaugeProviderFillFractionEmpty` for an empty gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimplegaugeprovider/fillfraction)*