# enable

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether to enable or disable the defroster.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * enable;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * enable;
```

## See Also

### Getting Details About the Defroster Settings to Set
- [var defroster: INCarDefroster](./defroster.md)
  The defroster to enable or disable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintent/enable-8tf0i)*