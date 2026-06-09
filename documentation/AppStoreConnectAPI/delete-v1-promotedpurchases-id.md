# Remove a promoted purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove a promotion for an in-app purchase or auto-renewable subscription from the App Store listing.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/promotedPurchases/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Promote a purchase](post-v1-promotedpurchases.md)
  Add an existing in-app purchase or auto-renewable subscription to the promoted in-app purchases on an app listing in the App Store.
- [List all promoted purchases for an app](get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted in-app purchases, including promoted auto-renewable subscriptions, for an app.
- [List promoted purchase ids for an app](get-v1-apps-_id_-relationships-promotedpurchases.md)
  Get a list of resource IDs representing promoted purchases for an auto-renewable subscription.
- [Read promoted purchase information](get-v1-promotedpurchases-_id_.md)
  Get details about a specific promoted in-app purchase.
- [Modify a promoted in-app purchase](patch-v1-promotedpurchases-_id_.md)
  Update the visibility of a promoted in-app purchase.
- [Modify the order of a promoted purchase for an app](patch-v1-apps-_id_-relationships-promotedpurchases.md)
  Update the order of promoted purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-promotedpurchases-_id_)*