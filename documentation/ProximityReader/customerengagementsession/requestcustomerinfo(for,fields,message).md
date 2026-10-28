# requestCustomerInfo(for:fields:message:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

Opens a form so that the customer can share the contact information.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final func requestCustomerInfo(for purpose: CustomerEngagementSession.Purpose? = nil, fields: [CustomerEngagementSession.Field], message: String? = nil) async throws -> CustomerEngagement.CustomerInfo
```

## Mentions

- [Adding support for Tap to Share to your app](../adding-support-for-tap-to-share-to-your-app.md)

## Return Value

[`CustomerEngagement.CustomerInfo`](../customerengagement/customerinfo.md) contact information shared by the customer.

## Discussion

If the `fields` array contains `pass` and a matching `passTypeIdentifier` , it displays the Wallet pass in full screen for the customer to confirm.

> **Throws**: [`CustomerEngagementSession.Error`](./error.md) if the request fails. Note: The merchant is responsible for obtaining appropriate consent and maintaining compliant privacy notices for personal information collected through this session.

## Parameters

- `purpose`: An optional enum of pre-defined purpose of the form, for example `.checkIn`. The `purpose`` parameter supports `.checkIn`and`.receipt`.
- `fields`: An array of contact field types on the form.
- `message`: A multi-line message text below the title.

## See Also

### Requesting and getting customer information
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](./requestsignup%28for,fields,message,emailconsent,smsconsent,termsandconditions%29.md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func requestAddress(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.Address](./requestaddress%28for,fields,message%29.md)
  Opens a form so that the customer can share the postal address and additionally collect email address and phone number.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](./requestpayment%28for,using,delegate%29.md)
  Opens a form so a customer can select a payment option.
- [CustomerEngagementSession.Purpose](./purpose.md)
  The purpose of a customer information request.
- [CustomerEngagementSession.Field](./field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.ConsentOption](./consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestcustomerinfo(for:fields:message:))*