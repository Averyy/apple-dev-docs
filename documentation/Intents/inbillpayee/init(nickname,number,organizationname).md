# init(nickname:number:organizationName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a payee object with the specified account details.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init?(nickname: INSpeakableString, number: String?, organizationName: INSpeakableString?)
```

```objc
- (instancetype) initWithNickname:(INSpeakableString *) nickname number:(NSString *) number organizationName:(INSpeakableString *) organizationName;
```

## Return Value

An initialized payee object.

## Discussion

When creating an [`INBillPayee`](../inbillpayee.md) object, specify the information that you need to identify a payee in your app.

## Parameters

- `nickname`: The nickname that the user assigned to this payee. Siri may display this text to the user. Don’t include account numbers or other potentially sensitive user information.
- `number`: A string to help the user differentiate between similar accounts. Typically, you use this parameter to specify the last few digits of the user’s account or an encoded version of the user’s account number. Never specify the user’s full account number.
- `organizationName`: The name of the organization receiving the payment. Siri may display this text to the user. Don’t include account numbers or other potentially sensitive user information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayee/init(nickname:number:organizationname:))*