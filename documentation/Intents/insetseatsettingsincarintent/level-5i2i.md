# level

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An integer value indicating the desired level for the seat setting.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * level;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * level;
```

#### Discussion

The value in this property maps to the heating, cooling, or massage level for the seat. For example, the value 1 corresponds to the first position of the corresponding knob, the value 2 corresponds to the second position of the knob, and so on. Use this property to change the corresponding seat setting to the level requested by the user.

The intent object contains a value for this property or the [`relativeLevelSetting`](./relativelevelsetting.md) property, but not both.

## See Also

### Getting the New Settings
- [enableCooling](./enablecooling-6bcu7.md)
  A Boolean value indicating whether to enable the seat cooling system.
- [enableHeating](./enableheating-5qj7i.md)
  A Boolean value indicating whether to enable the seat heating system.
- [enableMassage](./enablemassage-5jf2s.md)
  A Boolean value indicating whether to enable the seat massage system.
- [var relativeLevelSetting: INRelativeSetting](./relativelevelsetting.md)
  A relative change to the level value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintent/level-5i2i)*