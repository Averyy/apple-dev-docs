# fanSpeedPercentage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A floating-point value indicating the requested fan speed specified as a percentage of the maximum speed.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * fanSpeedPercentage;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * fanSpeedPercentage;
```

#### Discussion

Convert the value in this property to an appropriate fan speed setting in your vehicle. For example, if the user asks to set the fan speed to 50%, select a fan speed halfway between the minimum and maximum values.

This property is `nil` when the user modified a different climate control setting.

## See Also

### Getting the Fan Settings
- [enableFan](./enablefan-3bu9e.md)
  A Boolean value indicating whether to turn on the cabin fan system.
- [fanSpeedIndex](./fanspeedindex-4c1rr.md)
  An integer value indicating the desired fan speed position.
- [var relativeFanSpeedSetting: INRelativeSetting](./relativefanspeedsetting.md)
  A relative fan speed setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/fanspeedpercentage-ep0u)*