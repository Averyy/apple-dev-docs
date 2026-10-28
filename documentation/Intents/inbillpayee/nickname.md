# nickname

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user-defined name that identifies a bill-payment account in your app.

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
var nickname: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * nickname;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * nickname;
```

## Discussion

You should allow your users to assign custom nicknames to the payees they configure in your app. Nicknames let the user speak more naturally when talking to Siri. For example, the user might assign the nickname “cable” to an account associated with their cable television provider. When the user identifies a bill payee by its nickname, use this value to locate the corresponding account in your app.

> **Note**:  In your app, don’t let the user include account numbers or other potentially sensitive information in account nicknames.

## See Also

### Getting the Payee Details
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of the company that provides services to the user.
- [var accountNumber: String?](./accountnumber.md)
  A string to help the user differentiate between similar accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayee/nickname)*