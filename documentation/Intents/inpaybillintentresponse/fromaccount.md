# fromAccount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user account providing the funds.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var fromAccount: INPaymentAccount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INPaymentAccount * fromAccount;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INPaymentAccount * fromAccount;
```

#### Discussion

Use this property to specify information about the user account used to transfer funds. Siri may display the information in this object to the user at appropriate times. It’s your responsibility to handle the transfer of any funds from the specified account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponse/fromaccount)*