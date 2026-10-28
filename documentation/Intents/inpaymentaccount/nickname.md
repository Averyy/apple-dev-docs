# nickname

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user-defined name that identifies the account.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

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

A nickname is any string used to identify the account uniquely in your app. Ideally, your app should let users specify custom nicknames for their accounts. For example, the user might assign the nickname “business credit card” to the card they use to pay business-related expenses. When a nickname is present, use it to look up the account in your app.

## See Also

### Getting the Account Details
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of the organization that supplies the account to the user.
- [var accountType: INAccountType](./accounttype.md)
  The type of the account.
- [enum INAccountType](../inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [var accountNumber: String?](./accountnumber.md)
  A string to help the user differentiate between similar accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/nickname)*