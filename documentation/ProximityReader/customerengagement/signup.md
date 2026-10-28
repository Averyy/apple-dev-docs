# CustomerEngagement.SignUp

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

Contact information and marketing consent selections a customer provides during a sign-up request.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct SignUp
```

## Overview

You receive a `SignUp` value when [`requestSignup(for:fields:message:emailConsent:smsConsent:termsAndConditions:)`](../customerengagementsession/requestsignup%28for,fields,message,emailconsent,smsconsent,termsandconditions%29.md) completes successfully. The [`name`](./signup/name.md), [`phoneNumber`](./signup/phonenumber.md), and [`emailAddress`](./signup/emailaddress.md) properties are non`nil` only if you included the corresponding [`CustomerEngagementSession.Field`](../customerengagementsession/field.md) in the request and the customer chose to share it.

## Topics

### Getting sign-up details
- [let emailAddress: String?](./signup/emailaddress.md)
  The customer’s email address
- [let emailOptInSelection: Bool](./signup/emailoptinselection.md)
  A Boolean value that indicates if the customer opted-in to email marketing.
- [let name: PersonNameComponents?](./signup/name.md)
  The customer’s full name.
- [let phoneNumber: CNPhoneNumber?](./signup/phonenumber.md)
  The customer’s phone number.
- [let smsOptInSelection: Bool](./signup/smsoptinselection.md)
  A Boolean value that indicates if the customer opted-in to SMS marketing.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting customer information
- [CustomerEngagement.Address](./address.md)
  A customer’s address collected during a customer engagement session.
- [CustomerEngagement.CustomerInfo](./customerinfo.md)
  A response structure that describes customer information.
- [CustomerEngagement.ShoppingCart](./shoppingcart.md)
  A structure that describes the shopping cart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/signup)*