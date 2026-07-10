# requestSignup(for:fields:message:emailConsent:smsConsent:termsAndConditions:)

**Framework**: ProximityReader  
**Kind**: method

Opens a form so that the customer can share the contact information for the purpose of sign-up activity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func requestSignup(for purpose: CustomerEngagementSession.Purpose = .membership, fields: [CustomerEngagementSession.Field], message: String? = nil, emailConsent: CustomerEngagementSession.ConsentOption = .hidden, smsConsent: CustomerEngagementSession.ConsentOption = .hidden, termsAndConditions: String? = nil) async throws -> CustomerEngagement.SignUp
```

#### Return Value

[`CustomerEngagement.SignUp`](customerengagement/signup.md) contact information shared by the customer.

#### Discussion

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails.

## Parameters

- `purpose`: An enum of pre-defined purpose of the form for `.membership`, `.accountCreation`, and `.accountUpdate`. The default is `.membership`.
- `fields`: An array of contact field types on the form. Only `.emailAddress` and `.phoneNumber` types are supported.
- `message`: A multi-line message text below the title.
- `emailConsent`: A consent option to allow or decline promotions and offers over email channel.
- `smsConsent`: A consent option to allow or decline promotions and offers over SMS channel.
- `termsAndConditions`: An optional markdown string to display during the sign-up flow.

## See Also

- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](customerengagementsession/requestcustomerinfo(for:fields:message:).md)
  Opens a form so that the customer can share the contact information.
- [func requestAddress(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.Address](customerengagementsession/requestaddress(for:fields:message:).md)
  Opens a form so that the customer can share the postal address and additionally collect email address and phone number.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](customerengagementsession/requestpayment(for:using:delegate:).md)
  Opens a form so a customer can select a payment option.
- [CustomerEngagementSession.Purpose](customerengagementsession/purpose.md)
  The purpose of a customer information request.
- [CustomerEngagementSession.Field](customerengagementsession/field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.ConsentOption](customerengagementsession/consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestsignup(for:fields:message:emailconsent:smsconsent:termsandconditions:))*