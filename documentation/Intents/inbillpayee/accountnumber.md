# accountNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A string to help the user differentiate between similar accounts.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var accountNumber: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * accountNumber;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * accountNumber;
```

#### Discussion

The value of this property is a string that helps identify the payee to the user. Typically, this property contains a portion of the user’s account number with the payee, often in an obscured format such as `****123`. When resolving a payee requires disambiguation from among several values, you can display this string to the user to help identify each account.

## See Also

### Getting the Payee Details
- [var nickname: INSpeakableString?](./nickname.md)
  A user-defined name that identifies a bill-payment account in your app.
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of the company that provides services to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayee/accountnumber)*