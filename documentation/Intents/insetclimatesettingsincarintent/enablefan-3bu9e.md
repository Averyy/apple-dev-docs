# enableFan

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to turn on the cabin fan system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * enableFan;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * enableFan;
```

## Discussion

Enabling the fan typically disengages the automated climate control systems and causes the vehicle to enter a manual mode. Check the [`fanSpeedIndex`](./fanspeedindex-4c1rr.md), [`fanSpeedPercentage`](./fanspeedpercentage-ep0u.md), or [`relativeFanSpeedSetting`](./relativefanspeedsetting.md) properties to determine whether the user specified a speed for the fan.

This property is `nil` when the user modified a different climate control setting.

## See Also

### Getting the Fan Settings
- [fanSpeedIndex](./fanspeedindex-4c1rr.md)
  An integer value indicating the desired fan speed position.
- [fanSpeedPercentage](./fanspeedpercentage-ep0u.md)
  A floating-point value indicating the requested fan speed specified as a percentage of the maximum speed.
- [var relativeFanSpeedSetting: INRelativeSetting](./relativefanspeedsetting.md)
  A relative fan speed setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/enablefan-3bu9e)*