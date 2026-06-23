# CustomerEngagementSession

**Framework**: ProximityReader  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class CustomerEngagementSession
```

## Topics

### Structures
- [CustomerEngagementSession.Configuration](customerengagementsession/configuration-swift.struct.md)
  A set of configuration options for a customer engagement session.
- [CustomerEngagementSession.CustomerConfiguration](customerengagementsession/customerconfiguration-swift.struct.md)
  A structure that contains configuration details for the connected customer device.
- [CustomerEngagementSession.Token](customerengagementsession/token-swift.struct.md)
  A session token.
### Initializers
- [init(configuration: CustomerEngagementSession.Configuration)](customerengagementsession/init(configuration:).md)
  Creates a customer engagement session with the specified configuration.
### Instance Properties
- [let configuration: CustomerEngagementSession.Configuration](customerengagementsession/configuration-swift.property.md)
  Configuration for this session.
- [var customerConfiguration: CustomerEngagementSession.CustomerConfiguration?](customerengagementsession/customerconfiguration-swift.property.md)
  A structure containing configuration information of the customer device.
- [let events: any AsyncSequence<CustomerEngagementSession.Event, Never>](customerengagementsession/events.md)
  An asynchronous sequence of events that occur during the engagement session.
- [let token: CustomerEngagementSession.Token](customerengagementsession/token-swift.property.md)
  The session token.
### Instance Methods
- [func addPass(Data) async throws -> Bool](customerengagementsession/addpass(_:).md)
  Asks the customer to confirm adding a Pass to Wallet.
- [func close() async throws](customerengagementsession/close.md)
  Closes the engagement session.
- [func open(using: CustomerEngagement.Token?) async throws](customerengagementsession/open(using:).md)
  Opens the engagement session.
- [func requestAddress(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.Address](customerengagementsession/requestaddress(for:fields:message:).md)
  Opens a form so that the customer can share the postal address and additionally collect email address and phone number.
- [func requestCustomerInfo(for: CustomerEngagementSession.Purpose?, fields: [CustomerEngagementSession.Field], message: String?) async throws -> CustomerEngagement.CustomerInfo](customerengagementsession/requestcustomerinfo(for:fields:message:).md)
  Opens a form so that the customer can share the contact information.
- [func requestPayment(for: CustomerEngagement.ShoppingCartToken, using: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool](customerengagementsession/requestpayment(for:using:delegate:).md)
  Opens a form so a customer can select a payment option.
- [func requestSignup(for: CustomerEngagementSession.Purpose, fields: [CustomerEngagementSession.Field], message: String?, emailConsent: CustomerEngagementSession.ConsentOption, smsConsent: CustomerEngagementSession.ConsentOption, termsAndConditions: String?) async throws -> CustomerEngagement.SignUp](customerengagementsession/requestsignup(for:fields:message:emailconsent:smsconsent:termsandconditions:).md)
  Opens a form so that the customer can share the contact information for the purpose of sign-up activity.
- [func updateShoppingCart(CustomerEngagement.ShoppingCart) async throws -> CustomerEngagement.ShoppingCartToken](customerengagementsession/updateshoppingcart(_:).md)
  Updates the shopping cart on the customer’s device.
- [func updateStatus(CustomerEngagement.Status) async throws](customerengagementsession/updatestatus(_:).md)
  Updates the status on the customer’s screen.
### Enumerations
- [CustomerEngagementSession.ConsentOption](customerengagementsession/consentoption.md)
  An option on the sign-up form to receive promotional emails and text messages.
- [CustomerEngagementSession.Error](customerengagementsession/error.md)
  Errors that can occur during the engagement session.
- [CustomerEngagementSession.Event](customerengagementsession/event.md)
  Events that occur during a customer engagement session.
- [CustomerEngagementSession.Field](customerengagementsession/field.md)
  The contact information field in a customer request form.
- [CustomerEngagementSession.PeerClientType](customerengagementsession/peerclienttype.md)
  A value that indicates the type of connected peer client.
- [CustomerEngagementSession.Purpose](customerengagementsession/purpose.md)
  The purpose of a customer information request.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession)*