# PKDisbursementRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

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

```objc
@interface PKDisbursementRequest : NSObject
```

#### Overview

Use this object to create a disbursement (payment) request from a merchant to a user account — for example, a withdrawal from an online account.

## Topics

### Initializers
- [convenience init(merchantIdentifier: String, currency: Locale.Currency, region: Locale.Region, supportedNetworks: [PKPaymentNetwork], merchantCapabilities: PKMerchantCapability, summaryItems: [PKPaymentSummaryItem])](./pkdisbursementrequest/init%28merchantidentifier,currency,region,supportednetworks,merchantcapabilities,summaryitems%29.md)
  Creates a disbursement request with the parameters you specify.
- [- initWithMerchantIdentifier:currencyCode:regionCode:supportedNetworks:merchantCapabilities:summaryItems:](./pkdisbursementrequest/initwithmerchantidentifier_currencycode_regioncode_supportednetworks_merchantcapabilities_summaryitems_.md)
  Creates a new instance of a disbursement request with the merchant identifier, currency and region codes, and other parameters you specify.
### Setting currency and region information
- [var currency: Locale.Currency](./pkdisbursementrequest/currency.md)
  The currency to use for this disbursement.
- [var region: Locale.Region](./pkdisbursementrequest/region.md)
  The geographic region that describes the location for this disbursement.
- [var supportedRegions: [Locale.Region]?](./pkdisbursementrequest/supportedregions-1cl0f.md)
  An array of regions that describe the locations to support.
- [currencyCode](./pkdisbursementrequest/currencycode.md)
  The currency code string for this disbursement.
- [regionCode](./pkdisbursementrequest/regioncode.md)
  The merchant’s country code string.
- [supportedRegions](./pkdisbursementrequest/supportedregions-j9ug.md)
  An array of two-letter region codes that describes the regions to support.
### Setting the summary items
- [var summaryItems: [PKPaymentSummaryItem]](./pkdisbursementrequest/summaryitems.md)
  An array of payment summary item objects that the framework presents to people.
- [class PKPaymentSummaryItem](./pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
- [class PKDisbursementSummaryItem](./pkdisbursementsummaryitem.md)
  A summary item that represents a disbursement.
- [class PKInstantFundsOutFeeSummaryItem](./pkinstantfundsoutfeesummaryitem.md)
  A summary item that represents a fee for an instant funds out transfer.
### Setting custom application data
- [var applicationData: Data?](./pkdisbursementrequest/applicationdata.md)
  Optional merchant-supplied information about the disbursement request.
### Setting the merchant information
- [var merchantIdentifier: String](./pkdisbursementrequest/merchantidentifier.md)
  A string that identifies the merchant.
- [var merchantCapabilities: PKMerchantCapability](./pkdisbursementrequest/merchantcapabilities.md)
  A value that represents the payment-processing capabilities of the merchant.
- [var supportedNetworks: [PKPaymentNetwork]](./pkdisbursementrequest/supportednetworks.md)
  An array of payment networks the merchant supports.
### Requesting recipient contact fields
- [var recipientContact: PKContact?](./pkdisbursementrequest/recipientcontact.md)
  A contact object that describes the recipient.
- [var requiredRecipientContactFields: [PKContactField]](./pkdisbursementrequest/requiredrecipientcontactfields.md)
  An array that indicates which of the recipient’s contact details the merchant requires in order to process a disbursement.
### Excluding cards from the payment sheet
- [var unsupportedPrimaryAccountIdentifiers: [String]](./pkdisbursementrequest/unsupportedprimaryaccountidentifiers.md)
  An array of Apple Pay cards to exclude from payment.
### Handling errors
- [class func disbursementCardUnsupportedError() -> any Error](./pkdisbursementrequest/disbursementcardunsupportederror%28%29.md)
  Creates an error that indicates that the selected payment pass doesn’t support receiving funds through disbursements.
- [class func disbursementContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](./pkdisbursementrequest/disbursementcontactinvaliderror%28withcontactfield,localizeddescription%29.md)
  Creates a recipient contact error with the supplied field.
### Instance Properties
- [var isDelegatedRequest: Bool](./pkdisbursementrequest/isdelegatedrequest.md)
  A Boolean value that indicates whether this disbursement request is being made by a delegated entity on behalf of a merchant.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest)*