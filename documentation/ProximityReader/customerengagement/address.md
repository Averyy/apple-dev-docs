# CustomerEngagement.Address

**Framework**: ProximityReader  
**Kind**: struct

A customer’s address collected during a customer engagement session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct Address
```

## Topics

### Getting customer details
- [let emailAddress: String?](customerengagement/address/emailaddress.md)
  The customer’s email address.
- [let name: PersonNameComponents](customerengagement/address/name.md)
  The customer’s full name.
- [let phoneNumber: CNPhoneNumber?](customerengagement/address/phonenumber.md)
  The customer’s phone number.
- [let postalAddress: CNPostalAddress](customerengagement/address/postaladdress.md)
  The customer’s postal address.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [CustomerEngagement.CustomerInfo](customerengagement/customerinfo.md)
  A response structure that describes customer information.
- [CustomerEngagement.SignUp](customerengagement/signup.md)
  Contact information and marketing consent selections a customer provides during a sign-up request.
- [CustomerEngagement.ShoppingCart](customerengagement/shoppingcart.md)
  A structure that describes the shopping cart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/address)*