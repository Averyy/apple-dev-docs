# PKDisbursementRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents a request to disburse funds from a merchant to an individual.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class PKDisbursementRequest
```

#### Overview

Use this object to create a disbursement (payment) request from a merchant to a user account — for example, a withdrawal from an online account.

## Topics

### Initializers
- [convenience init(merchantIdentifier: String, currency: Locale.Currency, region: Locale.Region, supportedNetworks: [PKPaymentNetwork], merchantCapabilities: PKMerchantCapability, summaryItems: [PKPaymentSummaryItem])](pkdisbursementrequest/init(merchantidentifier:currency:region:supportednetworks:merchantcapabilities:summaryitems:).md)
  Creates a disbursement request with the parameters you specify.
### Setting currency and region information
- [var currency: Locale.Currency](pkdisbursementrequest/currency.md)
  The currency to use for this disbursement.
- [var region: Locale.Region](pkdisbursementrequest/region.md)
  The geographic region that describes the location for this disbursement.
- [var supportedRegions: [Locale.Region]?](pkdisbursementrequest/supportedregions-1cl0f.md)
  An array of regions that describe the locations to support.
### Setting the summary items
- [var summaryItems: [PKPaymentSummaryItem]](pkdisbursementrequest/summaryitems.md)
  An array of payment summary item objects that the framework presents to people.
- [class PKPaymentSummaryItem](pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
- [class PKDisbursementSummaryItem](pkdisbursementsummaryitem.md)
  A summary item that represents a disbursement.
- [class PKInstantFundsOutFeeSummaryItem](pkinstantfundsoutfeesummaryitem.md)
  A summary item that represents a fee for an instant funds out transfer.
### Setting custom application data
- [var applicationData: Data?](pkdisbursementrequest/applicationdata.md)
  Optional merchant-supplied information about the disbursement request.
### Setting the merchant information
- [var merchantIdentifier: String](pkdisbursementrequest/merchantidentifier.md)
  A string that identifies the merchant.
- [var merchantCapabilities: PKMerchantCapability](pkdisbursementrequest/merchantcapabilities.md)
  A value that represents the payment-processing capabilities of the merchant.
- [var supportedNetworks: [PKPaymentNetwork]](pkdisbursementrequest/supportednetworks.md)
  An array of payment networks the merchant supports.
### Requesting recipient contact fields
- [var recipientContact: PKContact?](pkdisbursementrequest/recipientcontact.md)
  A contact object that describes the recipient.
- [var requiredRecipientContactFields: [PKContactField]](pkdisbursementrequest/requiredrecipientcontactfields.md)
  An array that indicates which of the recipient’s contact details the merchant requires in order to process a disbursement.
### Handling errors
- [class func disbursementCardUnsupportedError() -> any Error](pkdisbursementrequest/disbursementcardunsupportederror.md)
  Creates an error that indicates that the selected payment pass doesn’t support receiving funds through disbursements.
- [class func disbursementContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](pkdisbursementrequest/disbursementcontactinvaliderror(withcontactfield:localizeddescription:).md)
  Creates a recipient contact error with the supplied field.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest)*