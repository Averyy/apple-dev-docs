# enableAirConditioner

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to turn on the air conditioner system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * enableAirConditioner;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * enableAirConditioner;
```

#### Discussion

This property is `nil` when the user modified a different climate control setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/enableairconditioner-3prnk)*