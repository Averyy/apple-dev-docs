# CustomerEngagement.SignUp

**Framework**: ProximityReader  
**Kind**: struct

Contact information and marketing consent selections a customer provides during a sign-up request.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct SignUp
```

#### Overview

You receive a `SignUp` value when [`requestSignup(for:fields:message:emailConsent:smsConsent:termsAndConditions:)`](customerengagementsession/requestsignup(for:fields:message:emailconsent:smsconsent:termsandconditions:).md) completes successfully. The [`name`](customerengagement/signup/name.md), [`phoneNumber`](customerengagement/signup/phonenumber.md), and [`emailAddress`](customerengagement/signup/emailaddress.md) properties are non`nil` only if you included the corresponding [`CustomerEngagementSession.Field`](customerengagementsession/field.md) in the request and the customer chose to share it.

## Topics

### Getting sign-up details
- [let emailAddress: String?](customerengagement/signup/emailaddress.md)
  The customer’s email address
- [let emailOptInSelection: Bool](customerengagement/signup/emailoptinselection.md)
  A Boolean value that indicates if the customer opted-in to email marketing.
- [let name: PersonNameComponents?](customerengagement/signup/name.md)
  The customer’s full name.
- [let phoneNumber: CNPhoneNumber?](customerengagement/signup/phonenumber.md)
  The customer’s phone number.
- [let smsOptInSelection: Bool](customerengagement/signup/smsoptinselection.md)
  A Boolean value that indicates if the customer opted-in to SMS marketing.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CustomerEngagement.Address](customerengagement/address.md)
  A customer’s address collected during a customer engagement session.
- [CustomerEngagement.CustomerInfo](customerengagement/customerinfo.md)
  Contact information and Wallet pass data shared by a customer during an engagement session.
- [CustomerEngagement.ShoppingCart](customerengagement/shoppingcart.md)
  A structure that describes the shopping cart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/signup)*