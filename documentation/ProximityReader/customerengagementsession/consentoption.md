# CustomerEngagementSession.ConsentOption

**Framework**: ProximityReader  
**Kind**: enum

An option on the sign-up form to receive promotional emails and text messages.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum ConsentOption
```

## Topics

### Enumeration Cases
- [CustomerEngagementSession.ConsentOption.hidden](customerengagementsession/consentoption/hidden.md)
  Hides the option.
- [CustomerEngagementSession.ConsentOption.preSelected](customerengagementsession/consentoption/preselected.md)
  Shows the customer the receive promotions option with a default preference.
- [CustomerEngagementSession.ConsentOption.visible](customerengagementsession/consentoption/visible.md)
  Shows the option with no default selected.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](customerengagementsession/requestcustomerinfo(for:fields:message:).md)
  Opens a form so that the customer can share the contact information.
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](customerengagementsession/requestsignup(for:fields:message:emailconsent:smsconsent:termsandconditions:).md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func requestAddress(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.Address](customerengagementsession/requestaddress(for:fields:message:).md)
  Opens a form so that the customer can share the postal address and additionally collect email address and phone number.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](customerengagementsession/requestpayment(for:using:delegate:).md)
  Opens a form so a customer can select a payment option.
- [CustomerEngagementSession.Purpose](customerengagementsession/purpose.md)
  The purpose of a customer information request.
- [CustomerEngagementSession.Field](customerengagementsession/field.md)
  The contact information field in a customer request form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/consentoption)*