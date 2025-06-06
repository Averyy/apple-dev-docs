# deleteSubscriptions

**Framework**: CloudKit JS  
**Kind**: method

Deletes one or more subscriptions.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.SubscriptionsResponse, CloudKit.CKError> deleteSubscriptions(
	CloudKit.Subscription|CloudKit.Subscription[]|String|String[] subscriptions
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.SubscriptionsResponse`](cloudkit.subscriptionsresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

See [`Modifying Subscriptions (subscriptions/modify)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ModifySubscriptions.html#//apple_ref/doc/uid/TP40015240-CH18) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Parameters

- `subscriptions`: Possible values are:

## See Also

- [saveSubscriptions](cloudkit.database/savesubscriptions.md)
  Saves one or more subscriptions to record changes.
- [fetchSubscriptions](cloudkit.database/fetchsubscriptions.md)
  Fetches one or more subscriptions.
- [fetchAllSubscriptions](cloudkit.database/fetchallsubscriptions.md)
  Fetches all subscriptions in the schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/deletesubscriptions)*