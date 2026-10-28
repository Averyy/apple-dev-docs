# accountType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of the account.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var accountType: INAccountType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INAccountType accountType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INAccountType accountType;
```

## Discussion

Use this property as needed to determine the type of the account. For example, you might need to handle transactions differently based on their type.

## See Also

### Getting the Account Details
- [var nickname: INSpeakableString?](./nickname.md)
  A user-defined name that identifies the account.
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of the organization that supplies the account to the user.
- [enum INAccountType](../inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [var accountNumber: String?](./accountnumber.md)
  A string to help the user differentiate between similar accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/accounttype)*