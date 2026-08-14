# CustomerEngagementSession.Purpose

**Framework**: ProximityReader  
**Kind**: enum

The purpose of a customer information request.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum Purpose
```

## Topics

### Enumeration Cases
- [CustomerEngagementSession.Purpose.accountCreation](customerengagementsession/purpose/accountcreation.md)
  A value indicating the merchant is requesting information for the customer to create an account.
- [CustomerEngagementSession.Purpose.accountUpdate](customerengagementsession/purpose/accountupdate.md)
  A value indicating the merchant is requesting information for the customer to update the account.
- [CustomerEngagementSession.Purpose.billing](customerengagementsession/purpose/billing.md)
  A value indicating the merchant is requesting billing information.
- [CustomerEngagementSession.Purpose.checkIn](customerengagementsession/purpose/checkin.md)
  A value indicating the merchant is requesting contact information for account lookup.
- [CustomerEngagementSession.Purpose.membership](customerengagementsession/purpose/membership.md)
  A value indicating the merchant is requesting information for the customer to sign-up for a membership.
- [CustomerEngagementSession.Purpose.receipt](customerengagementsession/purpose/receipt.md)
  A value indicating the merchant is requesting contact information for sending the receipt.
- [CustomerEngagementSession.Purpose.shipping](customerengagementsession/purpose/shipping.md)
  A value indicating the merchant is requesting shipping information.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](customerengagementsession/requestcustomerinfo(for:fields:message:).md)
  Opens a form so that the customer can share the contact information.
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](customerengagementsession/requestsignup(for:fields:message:emailconsent:smsconsent:termsandconditions:).md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func requestAddress(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.Address](customerengagementsession/requestaddress(for:fields:message:).md)
  Opens a form so that the customer can share the postal address and additionally collect email address and phone number.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](customerengagementsession/requestpayment(for:using:delegate:).md)
  Opens a form so a customer can select a payment option.
- [CustomerEngagementSession.Field](customerengagementsession/field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.ConsentOption](customerengagementsession/consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/purpose)*