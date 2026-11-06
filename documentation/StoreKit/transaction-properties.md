# Transaction properties

**Framework**: StoreKit  
**Role**: API Collection

The properties of a transaction, including identifiers, purchase and revocation dates and details, status, and offer details.

## Topics

### Getting the environment and storefront
- [let environment: AppStore.Environment](./transaction/environment.md)
  The server environment that generates and signs the transaction.
- [let storefront: Storefront](./transaction/storefront.md)
  The App Store storefront associated with the transaction.
### Getting the original transaction identifier
- [let originalID: UInt64](./transaction/originalid.md)
  The original transaction identifier of a purchase.
- [let originalPurchaseDate: Date](./transaction/originalpurchasedate.md)
  The date of purchase for the original transaction.
### Identifying a transaction
- [let id: UInt64](./transaction/id.md)
  The unique identifier for the transaction.
- [let webOrderLineItemID: String?](./transaction/weborderlineitemid.md)
  A unique ID that identifies subscription purchase events across devices, including subscription renewals.
### Identifying the app and product
- [let appBundleID: String](./transaction/appbundleid.md)
  The bundle identifier for the app.
- [let productID: String](./transaction/productid.md)
  The product identifier of the Apple In-App Purchase.
- [let productType: Product.ProductType](./transaction/producttype.md)
  The type of the Apple In-App Purchase.
- [let subscriptionGroupID: String?](./transaction/subscriptiongroupid.md)
  The identifier of the subscription group that the subscription belongs to.
### Getting purchase and expiration dates
- [let purchaseDate: Date](./transaction/purchasedate.md)
  The date that the App Store charged the user’s account for a purchased or restored product, or for a subscription purchase or renewal after a lapse.
- [let expirationDate: Date?](./transaction/expirationdate.md)
  The date the subscription expires or renews.
### Getting the product price and currency
- [var price: Decimal?](./transaction/price.md)
  The price of the Apple In-App Purchase that the system records in the transaction.
- [var currency: Locale.Currency?](./transaction/currency.md)
  The currency of the price of the product.
### Getting purchase details
- [let isUpgraded: Bool](./transaction/isupgraded.md)
  A Boolean that indicates whether the user upgraded to another subscription.
- [let ownershipType: Transaction.OwnershipType](./transaction/ownershiptype-swift.property.md)
  A value that indicates whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.
- [Transaction.OwnershipType](./transaction/ownershiptype-swift.struct.md)
  Values that indicate whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.
- [let purchasedQuantity: Int](./transaction/purchasedquantity.md)
  The number of purchased seats or consumable products.
### Getting multiseat information
- [let multiSeatInfo: Transaction.MultiSeatInfo?](./transaction/multiseatinfo-swift.property.md)
  The seat information for a multiseat subscription transaction.
- [Transaction.MultiSeatInfo](./transaction/multiseatinfo-swift.struct.md)
  The invitation model, price tiers, and revoked seats of a multiseat subscription transaction.
- [let additionalTransactionReason: Transaction.AdditionalTransactionReason?](./transaction/additionaltransactionreason-swift.property.md)
  The reason that more than one transaction represents the subscription period.
- [Transaction.AdditionalTransactionReason](./transaction/additionaltransactionreason-swift.struct.md)
  Reasons that more than one transaction represents a single subscription period.
### Getting subscription status
- [var subscriptionStatus: Product.SubscriptionInfo.Status?](./transaction/subscriptionstatus.md)
  An array that contains status information for a subscription group, including renewal and transaction information.
### Getting transaction reason
- [let reason: Transaction.Reason](./transaction/reason-swift.property.md)
  The cause of the purchase transaction, whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.
- [Transaction.Reason](./transaction/reason-swift.struct.md)
  A cause of a purchase transaction, indicating whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.
### Identifying offers
- [let offer: Transaction.Offer?](./transaction/offer-swift.property.md)
  The offer that applies to the transaction, including its offer type, payment mode, and ID.
- [Transaction.Offer](./transaction/offer-swift.struct.md)
  Discounts or promotions that apply to a transaction.
### Getting revocation status
- [let revocationDate: Date?](./transaction/revocationdate.md)
  The date that the App Store refunded or revoked the transaction.
- [let revocationReason: Transaction.RevocationReason?](./transaction/revocationreason-swift.property.md)
  The reason that the App Store refunded or revoked the transaction.
- [Transaction.RevocationReason](./transaction/revocationreason-swift.struct.md)
  Reasons that describe why the App Store may refund or revoke a transaction.
- [let revocationType: Transaction.RevocationType?](./transaction/revocationtype-swift.property.md)
  The type of refund or revocation that applies to the transaction.
- [Transaction.RevocationType](./transaction/revocationtype-swift.struct.md)
  The types of refunds and revocations that apply to transactions.
### Correlating transactions with accounts
- [let appAccountToken: UUID?](./transaction/appaccounttoken.md)
  A UUID that associates the transaction with a user on your own service.
### Getting the transaction information in JSON format
- [var jsonRepresentation: Data](./transaction/jsonrepresentation.md)
  The JSON representation of the transaction information.
### Deprecated
- [var currencyCode: String?](./transaction/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var environmentStringRepresentation: String](./transaction/environmentstringrepresentation.md)
  A string representation of the server environment.
- [var offerID: String?](./transaction/offerid.md)
  A string that identifies an offer applied to the current subscription.
- [var offerPaymentModeStringRepresentation: String?](./transaction/offerpaymentmodestringrepresentation.md)
  The string representation of the payment mode for a subscription offer.
- [var offerType: Transaction.OfferType?](./transaction/offertype-swift.property.md)
  The subscription offer type for the current subscription period.
- [var reasonStringRepresentation: String](./transaction/reasonstringrepresentation.md)
  The string representation of the transaction reason.
- [var storefrontCountryCode: String](./transaction/storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront of the purchase.

## See Also

### Transaction properties
- [var appTransactionID: String](./transaction/apptransactionid.md)
  The unique identifier of the app download transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction-properties)*