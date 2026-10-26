# enableMassage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to enable the seat massage system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
final var enableMassage: Bool? { get }
```

#### Discussion

This property is `nil` when the user modifies the heating or cooling settings.

## See Also

### Getting the New Settings
- [var enableCooling: Bool?](./enablecooling-8qqx3.md)
  A Boolean value indicating whether to enable the seat cooling system.
- [var enableHeating: Bool?](./enableheating-8auz2.md)
  A Boolean value indicating whether to enable the seat heating system.
- [var level: Int?](./level-94975.md)
  An integer value indicating the desired level for the seat setting.
- [var relativeLevelSetting: INRelativeSetting](./relativelevelsetting.md)
  A relative change to the level value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintent/enablemassage-46ndx)*