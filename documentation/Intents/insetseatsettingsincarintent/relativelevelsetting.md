# relativeLevelSetting

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A relative change to the level value.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var relativeLevelSetting: INRelativeSetting { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INRelativeSetting relativeLevelSetting;
```

*macOS*

```objc
@property (atomic, assign, readonly) INRelativeSetting relativeLevelSetting;
```

#### Discussion

Use this property to adjust the heating, cooling, or massage level to the next or previous setting. The value of this property is [`INRelativeSetting.unknown`](../inrelativesetting/unknown.md) when the user modified the [`level`](./level-5i2i.md) directly.

The intent object contains a value for this property or the [`level`](./level-5i2i.md) property, but not both.

## See Also

### Getting the New Settings
- [var enableCooling: Bool?](./enablecooling-8qqx3.md)
  A Boolean value indicating whether to enable the seat cooling system.
- [var enableHeating: Bool?](./enableheating-8auz2.md)
  A Boolean value indicating whether to enable the seat heating system.
- [var enableMassage: Bool?](./enablemassage-46ndx.md)
  A Boolean value indicating whether to enable the seat massage system.
- [var level: Int?](./level-94975.md)
  An integer value indicating the desired level for the seat setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintent/relativelevelsetting)*