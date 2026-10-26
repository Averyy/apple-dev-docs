# organizationName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the organization that supplies the account to the user.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var organizationName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * organizationName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * organizationName;
```

#### Discussion

This property contains the name of the bank or company that holds the user’s account. When the organization name is present, use it to look up the account in your app.

## See Also

### Getting the Account Details
- [var nickname: INSpeakableString?](./nickname.md)
  A user-defined name that identifies the account.
- [var accountType: INAccountType](./accounttype.md)
  The type of the account.
- [enum INAccountType](../inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [var accountNumber: String?](./accountnumber.md)
  A string to help the user differentiate between similar accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/organizationname)*