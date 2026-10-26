# accountNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A string to help the user differentiate between similar accounts.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

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

The value of this property is a string that helps identify the account to the user. Typically, this property contains a portion of the user’s account number, often in an obscured format such as `****1234`. When resolving an account requires disambiguation from among several values, display this string to the user to help identify each account.

## See Also

### Getting the Account Details
- [var nickname: INSpeakableString?](./nickname.md)
  A user-defined name that identifies the account.
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of the organization that supplies the account to the user.
- [var accountType: INAccountType](./accounttype.md)
  The type of the account.
- [enum INAccountType](../inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/accountnumber)*