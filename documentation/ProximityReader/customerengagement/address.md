# CustomerEngagement.Address

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A customer’s address collected during a customer engagement session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct Address
```

## Topics

### Getting customer details
- [let emailAddress: String?](./address/emailaddress.md)
  The customer’s email address.
- [let name: PersonNameComponents](./address/name.md)
  The customer’s full name.
- [let phoneNumber: CNPhoneNumber?](./address/phonenumber.md)
  The customer’s phone number.
- [let postalAddress: CNPostalAddress](./address/postaladdress.md)
  The customer’s postal address.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting customer information
- [CustomerEngagement.CustomerInfo](./customerinfo.md)
  A response structure that describes customer information.
- [CustomerEngagement.SignUp](./signup.md)
  Contact information and marketing consent selections a customer provides during a sign-up request.
- [CustomerEngagement.ShoppingCart](./shoppingcart.md)
  A structure that describes the shopping cart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement/address)*