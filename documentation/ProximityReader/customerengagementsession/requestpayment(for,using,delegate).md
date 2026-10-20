# requestPayment(for:using:delegate:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

Opens a form so a customer can select a payment option.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
final func requestPayment(for shoppingCartToken: CustomerEngagement.ShoppingCartToken, using paymentRequest: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool
```

## Mentions

- [Adding support for Tap to Share to your app](../adding-support-for-tap-to-share-to-your-app.md)

## See Also

### Requesting and getting customer information
- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](./requestcustomerinfo%28for,fields,message%29.md)
  Opens a form so that the customer can share the contact information.
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](./requestsignup%28for,fields,message,emailconsent,smsconsent,termsandconditions%29.md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func requestAddress(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.Address](./requestaddress%28for,fields,message%29.md)
  Opens a form so that the customer can share the postal address and additionally collect email address and phone number.
- [CustomerEngagementSession.Purpose](./purpose.md)
  The purpose of a customer information request.
- [CustomerEngagementSession.Field](./field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.ConsentOption](./consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestpayment(for:using:delegate:))*