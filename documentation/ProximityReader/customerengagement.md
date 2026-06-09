# CustomerEngagement

**Framework**: ProximityReader  
**Kind**: enum

An enumeration of the shared data between the merchant and customer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum CustomerEngagement
```

#### Overview

Use this enumeration to authenticate credentials, display customer screen states, and get customer information.

## Topics

### Creating authentication credentials
- [CustomerEngagement.Token](customerengagement/token.md)
  A token that authenticates access to a customer engagement session.
### Providing shopping cart token for payment request
- [CustomerEngagement.ShoppingCartToken](customerengagement/shoppingcarttoken.md)
  A token referencing the shopping cart.
### Displaying customer screen states
- [CustomerEngagement.Status](customerengagement/status.md)
  A predefined set of customer engagement screen states.
### Getting customer information
- [CustomerEngagement.Address](customerengagement/address.md)
  A customer’s address collected during a customer engagement session.
- [CustomerEngagement.CustomerInfo](customerengagement/customerinfo.md)
  Contact information and Wallet pass data shared by a customer during an engagement session.
- [CustomerEngagement.SignUp](customerengagement/signup.md)
  Contact information and marketing consent selections a customer provides during a sign-up request.
- [CustomerEngagement.ShoppingCart](customerengagement/shoppingcart.md)
  A structure that describes the shopping cart content.

## See Also

- [Adding support for Tap to Share to your app](adding-support-for-tap-to-share-to-your-app.md)
  Request and share customer information on device.
- [class CustomerEngagementSession](customerengagementsession.md)
  The object you use to share and request customer information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagement)*