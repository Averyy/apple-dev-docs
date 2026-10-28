# requestAddress(for:fields:message:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

Opens a form so that the customer can share the postal address and additionally collect email address and phone number.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final func requestAddress(for purpose: CustomerEngagementSession.Purpose? = nil, fields: [CustomerEngagementSession.Field], message: String? = nil) async throws -> CustomerEngagement.Address
```

## Return Value

[`CustomerEngagement.Address`](../customerengagement/address.md) with postal address and contact information shared by the customer.

## Discussion

For example, email and phone number can be used for delivery notification.

> **Throws**: [`CustomerEngagementSession.Error`](./error.md) if the request fails.

## Parameters

- `purpose`: An optional enum of pre-defined purpose of the form, for example `.shipping`.
- `fields`: An array of optional contact field types on the form. Only `.emailAddress` and `.phoneNumber` types are supported.
- `message`: A multi-line message text below the title.

## See Also

### Requesting and getting customer information
- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](./requestcustomerinfo%28for,fields,message%29.md)
  Opens a form so that the customer can share the contact information.
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](./requestsignup%28for,fields,message,emailconsent,smsconsent,termsandconditions%29.md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](./requestpayment%28for,using,delegate%29.md)
  Opens a form so a customer can select a payment option.
- [CustomerEngagementSession.Purpose](./purpose.md)
  The purpose of a customer information request.
- [CustomerEngagementSession.Field](./field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.ConsentOption](./consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestaddress(for:fields:message:))*