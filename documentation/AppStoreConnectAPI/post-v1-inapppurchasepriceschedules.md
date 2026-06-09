# Add a Scheduled Price Change to an In-App Purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a scheduled price change for an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing in-app purchases](managing-in-app-purchases.md)

#### Discussion

> **Note**:  A base territory is now required when adding or creating a price for an in-app purchase.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/inAppPurchasePriceSchedules`

## See Also

- [Read In-App Purchase Price Schedule Information](get-v1-inapppurchasepriceschedules-_id_.md)
  Get information about a specific scheduled price change for an in-app purchase.
- [Read Price Information for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-manualprices.md)
  Get information about a set price or prices for an in-app purchase price schedule.
- [List manual price IDs for an in-app purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-manualprices.md)
- [List Automatically Generated Prices for an In-App Purchase Price](get-v1-inapppurchasepriceschedules-_id_-automaticprices.md)
  Get information about a price or prices automatically set based on a base territory for an in-app purchase price schedule.
- [List automatic price IDs for an in-app purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-automaticprices.md)
- [Read the Selected Base Territory for an In-App Purchase Price Schedule](get-v1-inapppurchasepriceschedules-_id_-baseterritory.md)
  Get information about the selected base territory for an in-app purchase price schedule.
- [Get the base territory ID for an in-app purchase price schedule](get-v1-inapppurchasepriceschedules-_id_-relationships-baseterritory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-inapppurchasepriceschedules)*