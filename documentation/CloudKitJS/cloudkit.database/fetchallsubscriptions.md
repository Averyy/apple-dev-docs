# fetchAllSubscriptions

**Framework**: CloudKit JS  
**Kind**: method

Fetches all subscriptions in the schema.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.SubscriptionsResponse, CloudKit.CKError> fetchAllSubscriptions();
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.SubscriptionsResponse`](cloudkit.subscriptionsresponse.md) object , or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

See [`Fetching Subscriptions (subscriptions/list)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GetSubscriptions.html#//apple_ref/doc/uid/TP40015240-CH16) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## See Also

- [saveSubscriptions](cloudkit.database/savesubscriptions.md)
  Saves one or more subscriptions to record changes.
- [fetchSubscriptions](cloudkit.database/fetchsubscriptions.md)
  Fetches one or more subscriptions.
- [deleteSubscriptions](cloudkit.database/deletesubscriptions.md)
  Deletes one or more subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchallsubscriptions)*