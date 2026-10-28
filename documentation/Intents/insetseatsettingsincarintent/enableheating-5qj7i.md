# enableHeating

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to enable the seat heating system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * enableHeating;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * enableHeating;
```

## Discussion

This property is `nil` when the user modifies the cooling or massage settings.

## See Also

### Getting the New Settings
- [enableCooling](./enablecooling-6bcu7.md)
  A Boolean value indicating whether to enable the seat cooling system.
- [enableMassage](./enablemassage-5jf2s.md)
  A Boolean value indicating whether to enable the seat massage system.
- [level](./level-5i2i.md)
  An integer value indicating the desired level for the seat setting.
- [var relativeLevelSetting: INRelativeSetting](./relativelevelsetting.md)
  A relative change to the level value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintent/enableheating-5qj7i)*