# relativeFanSpeedSetting

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A relative fan speed setting.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var relativeFanSpeedSetting: INRelativeSetting { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INRelativeSetting relativeFanSpeedSetting;
```

*macOS*

```objc
@property (atomic, assign, readonly) INRelativeSetting relativeFanSpeedSetting;
```

#### Discussion

Use this property to adjust the fan speed to the next or previous setting. The value of this property is [`INRelativeSetting.unknown`](../inrelativesetting/unknown.md) when the user modified a different climate control setting.

## See Also

### Getting the Fan Settings
- [var enableFan: Bool?](./enablefan-5srs9.md)
  A Boolean value indicating whether to turn on the cabin fan system.
- [var fanSpeedIndex: Int?](./fanspeedindex-wz49.md)
  An integer value indicating the desired fan speed position.
- [var fanSpeedPercentage: Double?](./fanspeedpercentage-7i2hq.md)
  A floating-point value indicating the requested fan speed specified as a percentage of the maximum speed.
- [enableFan](./enablefan-3bu9e.md)
  A Boolean value indicating whether to turn on the cabin fan system.
- [fanSpeedIndex](./fanspeedindex-4c1rr.md)
  An integer value indicating the desired fan speed position.
- [fanSpeedPercentage](./fanspeedpercentage-ep0u.md)
  A floating-point value indicating the requested fan speed specified as a percentage of the maximum speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/relativefanspeedsetting)*