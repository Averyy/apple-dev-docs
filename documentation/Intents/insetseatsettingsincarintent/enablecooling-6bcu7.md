# enableCooling

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to enable the seat cooling system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * enableCooling;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * enableCooling;
```

#### Discussion

This property is `nil` when the user modifies the heating or massage settings.

## See Also

### Getting the New Settings
- [enableHeating](./enableheating-5qj7i.md)
  A Boolean value indicating whether to enable the seat heating system.
- [enableMassage](./enablemassage-5jf2s.md)
  A Boolean value indicating whether to enable the seat massage system.
- [level](./level-5i2i.md)
  An integer value indicating the desired level for the seat setting.
- [var relativeLevelSetting: INRelativeSetting](./relativelevelsetting.md)
  A relative change to the level value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintent/enablecooling-6bcu7)*