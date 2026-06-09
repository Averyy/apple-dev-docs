# CustomerEngagement.CustomerInfo

**Framework**: ProximityReader  
**Kind**: struct

Contact information and Wallet pass data shared by a customer during an engagement session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct CustomerInfo
```

#### Overview

You receive a `CustomerInfo` value when                    [`requestCustomerInfo(for:fields:message:)`](customerengagementsession/requestcustomerinfo(for:fields:message:).md) successfully completes. Each property is non`nil` only if you included the corresponding [`CustomerEngagementSession.Field`](customerengagementsession/field.md) in the request and the customer chose to share it.

## Topics

### Getting customer information details
- [let barcodeMessage: String?](customerengagement/customerinfo/barcodemessage.md)
  A message for the barcode.
- [let customerVASData: Data?](customerengagement/customerinfo/customervasdata.md)
  The encrypted VAS content of a selected Wallet pass.
- [let emailAddress: String?](customerengagement/customerinfo/emailaddress.md)
  The customer’s email address or Hide My Email address if supported.
- [let phoneNumber: CNPhoneNumber?](customerengagement/customerinfo/phonenumber.md)
  The customer’s phone number, if provided.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CustomerEngagement.Address](customerengagement/address.md)
  A customer’s address collected during a customer engagement session.
- [CustomerEngagement.SignUp](customerengagement/signup.md)
  Contact information and marketing consent selections a customer provides during a sign-up request.
- [CustomerEngagement.ShoppingCart](customerengagement/shoppingcart.md)
  A structure that describes the shopping cart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/customerinfo)*