# CustomerEngagementSession.Purpose

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

The purpose of a customer information request.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum Purpose
```

## Topics

### Enumeration Cases
- [CustomerEngagementSession.Purpose.accountCreation](./purpose/accountcreation.md)
  A value indicating the merchant is requesting information for the customer to create an account.
- [CustomerEngagementSession.Purpose.accountUpdate](./purpose/accountupdate.md)
  A value indicating the merchant is requesting information for the customer to update the account.
- [CustomerEngagementSession.Purpose.billing](./purpose/billing.md)
  A value indicating the merchant is requesting billing information.
- [CustomerEngagementSession.Purpose.checkIn](./purpose/checkin.md)
  A value indicating the merchant is requesting contact information for account lookup.
- [CustomerEngagementSession.Purpose.membership](./purpose/membership.md)
  A value indicating the merchant is requesting information for the customer to sign-up for a membership.
- [CustomerEngagementSession.Purpose.receipt](./purpose/receipt.md)
  A value indicating the merchant is requesting contact information for sending the receipt.
- [CustomerEngagementSession.Purpose.shipping](./purpose/shipping.md)
  A value indicating the merchant is requesting shipping information.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting and getting customer information
- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](./requestcustomerinfo%28for,fields,message%29.md)
  Opens a form so that the customer can share the contact information.
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](./requestsignup%28for,fields,message,emailconsent,smsconsent,termsandconditions%29.md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func requestAddress(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.Address](./requestaddress%28for,fields,message%29.md)
  Opens a form so that the customer can share the postal address and additionally collect email address and phone number.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](./requestpayment%28for,using,delegate%29.md)
  Opens a form so a customer can select a payment option.
- [CustomerEngagementSession.Field](./field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.ConsentOption](./consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/purpose)*