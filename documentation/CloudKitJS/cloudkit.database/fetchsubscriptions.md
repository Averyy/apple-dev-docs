# fetchSubscriptions

**Framework**: CloudKit JS  
**Kind**: method

Fetches one or more subscriptions.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.SubscriptionsResponse, CloudKit.CKError> fetchSubscriptions(
	CloudKit.Subscription|CloudKit.Subscription[]|String|String[] subscriptions
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.SubscriptionsResponse`](cloudkit.subscriptionsresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

See [`Fetching Subscriptions by Identifier (subscriptions/lookup)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/LookupSubscriptionsbyID.html#//apple_ref/doc/uid/TP40015240-CH17) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Parameters

- `subscriptions`: Possible values are:

## See Also

- [saveSubscriptions](cloudkit.database/savesubscriptions.md)
  Saves one or more subscriptions to record changes.
- [fetchAllSubscriptions](cloudkit.database/fetchallsubscriptions.md)
  Fetches all subscriptions in the schema.
- [deleteSubscriptions](cloudkit.database/deletesubscriptions.md)
  Deletes one or more subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchsubscriptions)*