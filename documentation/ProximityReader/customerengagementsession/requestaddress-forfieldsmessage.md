# requestAddress(for:fields:message:)

**Framework**: ProximityReader  
**Kind**: method

Opens a form so that the customer can share the postal address and additionally collect email address and phone number.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func requestAddress(for purpose: CustomerEngagementSession.Purpose? = nil, fields: [CustomerEngagementSession.Field], message: String? = nil) async throws -> CustomerEngagement.Address
```

#### Return Value

[`CustomerEngagement.Address`](customerengagement/address.md) with postal address and contact information shared by the customer.

#### Discussion

For example, email and phone number can be used for delivery notification.

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails.

## Parameters

- `purpose`: An optional enum of pre-defined purpose of the form, for example `.shipping`.
- `fields`: An array of optional contact field types on the form. Only `.emailAddress` and `.phoneNumber` types are supported.
- `message`: A multi-line message text below the title.

## See Also

- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](customerengagementsession/requestcustomerinfo(for:fields:message:).md)
  Opens a form so that the customer can share the contact information.
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](customerengagementsession/requestsignup(for:fields:message:emailconsent:smsconsent:termsandconditions:).md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](customerengagementsession/requestpayment(for:using:delegate:).md)
  Opens a form so a customer can select a payment option.
- [CustomerEngagementSession.Purpose](customerengagementsession/purpose.md)
  The purpose of a customer information request.
- [CustomerEngagementSession.Field](customerengagementsession/field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.ConsentOption](customerengagementsession/consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestaddress(for:fields:message:))*