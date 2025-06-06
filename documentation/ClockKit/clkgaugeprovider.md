# CLKGaugeProvider

**Framework**: ClockKit  
**Kind**: class

An abstract superclass that provides all the common behaviors for the gauge providers.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKGaugeProvider
```

#### Overview

Don’t create instances of this class yourself. Instead, create instances of the concrete subclasses based on the type of gauge you’re trying to create.

## Topics

### Setting the Gauge’s Appearance
- [var gaugeColors: [UIColor]?](clkgaugeprovider/gaugecolors.md)
  The colors of the gauge.
- [var gaugeColorLocations: [NSNumber]?](clkgaugeprovider/gaugecolorlocations.md)
  The location of each color in a multicolor gauge’s gradient.
- [var style: CLKGaugeProviderStyle](clkgaugeprovider/style.md)
  The style that defines the gauge’s appearance.
### Adding Accessibility
- [var accessibilityLabel: String?](clkgaugeprovider/accessibilitylabel.md)
  A localized string that describes the gague.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CLKSimpleGaugeProvider](clksimplegaugeprovider.md)
- [CLKTimeIntervalGaugeProvider](clktimeintervalgaugeprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKSimpleGaugeProvider](clksimplegaugeprovider.md)
  A gauge that shows a fractional value.
- [class CLKTimeIntervalGaugeProvider](clktimeintervalgaugeprovider.md)
  A gauge that tracks time intervals.
- [let CLKSimpleGaugeProviderFillFractionEmpty: Float](clksimplegaugeproviderfillfractionempty.md)
  A fill value indicating an empty gauge.
- [enum CLKGaugeProviderStyle](clkgaugeproviderstyle.md)
  Visual styles available for gauges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkgaugeprovider)*