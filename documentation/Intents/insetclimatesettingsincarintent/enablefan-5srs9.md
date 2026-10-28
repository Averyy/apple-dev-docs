# enableFan

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to turn on the cabin fan system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
final var enableFan: Bool? { get }
```

## Discussion

Enabling the fan typically disengages the automated climate control systems and causes the vehicle to enter a manual mode. Check the [`fanSpeedIndex`](./fanspeedindex-4c1rr.md), [`fanSpeedPercentage`](./fanspeedpercentage-ep0u.md), or [`relativeFanSpeedSetting`](./relativefanspeedsetting.md) properties to determine whether the user specified a speed for the fan.

This property is `nil` when the user modified a different climate control setting.

## See Also

### Getting the Fan Settings
- [var fanSpeedIndex: Int?](./fanspeedindex-wz49.md)
  An integer value indicating the desired fan speed position.
- [var fanSpeedPercentage: Double?](./fanspeedpercentage-7i2hq.md)
  A floating-point value indicating the requested fan speed specified as a percentage of the maximum speed.
- [var relativeFanSpeedSetting: INRelativeSetting](./relativefanspeedsetting.md)
  A relative fan speed setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/enablefan-5srs9)*