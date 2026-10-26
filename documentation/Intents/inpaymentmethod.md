# INPaymentMethod

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Information about a form of payment supported by your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPaymentMethod
```

```objc
@interface INPaymentMethod : NSObject
```

#### Overview

An [`INPaymentMethod`](./inpaymentmethod.md) object describes a way in which a user can pay for services. A payment method object stores information that you can display to the user when choosing payment options. Specifically, the object stores information about the type of payment, the name of the payment service, and an icon for any related brand information. Typical payment methods include credit cards and bank accounts. For example, you would use a payment method object to specify information about a brand of credit card that you support.

You create payment method objects as needed and include them in any appropriate response objects. The names of payment methods in a single response should be different to avoid confusion, but their types may still be the same. For example, you can have multiple credit card payment methods as long as each one has a unique name.

> **Note**:  You do not use payment methods to process actual payments from the user. You are responsible for handling any financial transactions from your app or Intents extension.

## Topics

### Initializing a Payment Object
- [init(type: INPaymentMethodType, name: String?, identificationHint: String?, icon: INImage?)](./inpaymentmethod/init%28type,name,identificationhint,icon%29.md)
  Initializes the payment method object with the specified type and descriptive information.
- [class func applePay() -> Self](./inpaymentmethod/applepay%28%29.md)
  Creates and returns a payment method object that represents payment through Apple Pay.
### Getting the Payment Information
- [var type: INPaymentMethodType](./inpaymentmethod/type.md)
  The type of account used as the source of funds.
- [enum INPaymentMethodType](./inpaymentmethodtype.md)
  Constants describing the available payment options.
- [var name: String?](./inpaymentmethod/name.md)
  The name of this payment type.
- [var identificationHint: String?](./inpaymentmethod/identificationhint.md)
  The hint for identifying the payment method.
- [var icon: INImage?](./inpaymentmethod/icon.md)
  The image representing the payment method.
### Initializers
- [init?(coder: NSCoder)](./inpaymentmethod/init%28coder%29.md)

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

### Data Objects
- [enum INAccountType](./inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [class INCurrencyAmount](./incurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [class INPaymentAccount](./inpaymentaccount.md)
  A user account that provides the funds when making a payment.
- [class INPaymentAmount](./inpaymentamount.md)
  The amount of money to apply to a bill payment.
- [class INPaymentRecord](./inpaymentrecord.md)
  Detailed information about a financial transaction made between two users.
- [enum INPaymentStatus](./inpaymentstatus.md)
  Constants indicating the state of the financial transaction.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethod)*