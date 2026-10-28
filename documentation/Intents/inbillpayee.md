# INBillPayee

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The entity that receives the proceeds from a bill payment.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INBillPayee
```

```objc
@interface INBillPayee : NSObject
```

## Overview

An [`INBillPayee`](./inbillpayee.md) object describes an entity that receives payment for a bill. When the user asks Siri to pay a bill, use this information to identify the entity receiving the payment. For example, a payee might represent a utility for which the user has already registered a bill payment option. Users must configure payees in advance using your app. This object contains information that you use to identify one of those preconfigured accounts.

> **Note**:  When configuring bill-pay options in your app, don’t include the user’s account number in the organization name and don’t let the user specify other sensitive personal information in account nicknames. Siri can display nicknames and organization names and these should never contain any sensitive personal information.

## Topics

### Initializing the Payee Object
- [init?(nickname: INSpeakableString, number: String?, organizationName: INSpeakableString?)](./inbillpayee/init%28nickname,number,organizationname%29.md)
  Initializes a payee object with the specified account details.
### Getting the Payee Details
- [var nickname: INSpeakableString?](./inbillpayee/nickname.md)
  A user-defined name that identifies a bill-payment account in your app.
- [var organizationName: INSpeakableString?](./inbillpayee/organizationname.md)
  The name of the company that provides services to the user.
- [var accountNumber: String?](./inbillpayee/accountnumber.md)
  A string to help the user differentiate between similar accounts.
### Initializers
- [init?(coder: NSCoder)](./inbillpayee/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Bill Data Objects
- [class INBillDetails](./inbilldetails.md)
  The detailed information associated with a bill.
- [class INBillTypeResolutionResult](./inbilltyperesolutionresult.md)
  A resolution result for the types of bills a user might pay.
- [class INBillPayeeResolutionResult](./inbillpayeeresolutionresult.md)
  A resolution result for the recipient of a bill payment.
- [class INVisualCodeTypeResolutionResult](./invisualcodetyperesolutionresult.md)
  A resolution result for the type of visual code used to exchange information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbillpayee)*