# offer_code_ref_name

**Framework**: App Store Receipts  
**Kind**: typealias

The offer-reference name of the subscription offer code that the customer redeems.

**Availability**:
- App Store Receipts 1.4+

## Declaration

```swift
string offer_code_ref_name
```

#### Discussion

When a customer successfully redeems an offer code, this field is present in the receipt and contains the reference name of the offer. You establish the offer reference name in App Store Connect when you configure offers and create the offer codes. For more information about setting up offers, see [`Set Up Offer Codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev6a098e4b1).

Use this value to:

- Determine whether the sale of the subscription was from an offer code campaign.
- Determine the specific offer the customer redeemed.
- Keep track of subscription-offer codes a customer has redeemed, to limit discounts you offer, according to your business model.

For more information on offers and offer codes, see [`Implementing offer codes in your app`](https://developer.apple.com/documentation/StoreKit/implementing-offer-codes-in-your-app).

## See Also

- [type promotional_offer_id](promotional_offer_id.md)
  The identifier of the promotional offer for an auto-renewable subscription that the user redeems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/offer_code_ref_name)*