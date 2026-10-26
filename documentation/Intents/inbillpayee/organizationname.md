# organizationName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the company that provides services to the user.

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

This property represents the actual name of the organization that provides services to the user and supports bill payment through your app. The organization name might refer to the name of a specific company or group that provides services. When the user specifies the organization name, instead of the account nickname, use this value to locate the corresponding account in your app.

> **Note**:  In your app, don’t include account numbers or other potentially sensitive user information in organization names.

## See Also

### Getting the Payee Details
- [var nickname: INSpeakableString?](./nickname.md)
  A user-defined name that identifies a bill-payment account in your app.
- [var accountNumber: String?](./accountnumber.md)
  A string to help the user differentiate between similar accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayee/organizationname)*