# saveSubscriptions

**Framework**: CloudKit JS  
**Kind**: method

Saves one or more subscriptions to record changes.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.SubscriptionsResponse, CloudKit.CKError> saveSubscriptions(
	CloudKit.Subscription|CloudKit.Subscription[] subscriptions
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.SubscriptionsResponse`](cloudkit.subscriptionsresponse.md) object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Instead of fetching records, you can subscribe to changes, and let the server run the query in the background. You subscribe to changes by creating a subscription, represented by a [`CloudKit.Subscription`](cloudkit.subscription.md) dictionary, and saving it to a database. Then you register for push notifications and handle them when they arrive.

Subscribing to Zone Changes

To subscribe to all changes in a zone, set the [`CloudKit.Subscription`](cloudkit.subscription.md) dictionary’s `subscriptionType` key to `zone` and set the `zoneID` key to the name of the zone you want to observe.

```javascript
var zoneSubscription = {
    subscriptionType: 'zone',
    subscriptionID: 'changedArtwork',
    zoneID: { zoneName: 'publicArtwork' }
};
```

Save the subscription using the [`saveSubscriptions`](cloudkit.database/savesubscriptions.md) method.

```javascript
database.saveSubscriptions(zoneSubscription).then(function(response) {
    if (response.hasErrors) {
        // Insert error handling
        throw response.errors[0];
    } else {
        // Successfully saved subscription
    }
});
```

To get the saved subscription, use the [`subscriptions`](cloudkit.subscriptionsresponse/subscriptions.md) property in the [`CloudKit.SubscriptionsResponse`](cloudkit.subscriptionsresponse.md) class.

Subscribing to Record Changes Using a Query

Create a query subscription object (a [`CloudKit.Subscription`](cloudkit.subscription.md) dictionary with the `subscriptionType` key set to `query`) specifying the record type, matching criteria, and types of changes you want to be notified about. Then save the query subscription object to the database.

For example, subscribe to receive new artwork from an artist where the `artist` field in the `Artwork` record type is a `Reference` type. First create a reference to the `Artist` record to use in the query.

```javascript
var artistReference = {
    action: 'NONE',
    recordName: 'Mei Chen'
}
```

> **Note**:  Because the record name is a unique identifier, you can create the `Reference` object containing just the `recordName` and `action` key. A query subscription with a `Reference` field requires an `action` key.

 Because the record name is a unique identifier, you can create the `Reference` object containing just the `recordName` and `action` key. A query subscription with a `Reference` field requires an `action` key.

Create a query subscription object specifying `Artwork` records whose `artist` field matches the `Reference` object. Use the `firesOn` key to specify the types of operations that fire this subscription.

```javascript
var querySubscription = {
    subscriptionType: 'query',
    firesOn: ['create', 'update', 'delete'],
    query: {
        recordType: 'Artwork',
        filterBy: [{
           fieldName: 'artist',
           comparator: 'EQUALS',
           fieldValue: { value: artistReference }
        }]
    }
};
```

Save the subscription using the [`saveSubscriptions`](cloudkit.database/savesubscriptions.md) method and get the saved subscription using the [`subscriptions`](cloudkit.subscriptionsresponse/subscriptions.md) property in the [`CloudKit.SubscriptionsResponse`](cloudkit.subscriptionsresponse.md) class.

```javascript
database.saveSubscriptions(querySubscription).then(function(response) {
    if (response.hasErrors) {
        // Insert error handling
        throw response.errors[0];
    } else {
        // Successfully saved subscription
    }
});
```

Handling Subscription Push Notifications

Add a notification listener to the app’s container using the [`addNotificationListener`](cloudkit.container/addnotificationlistener.md) method in the [`CloudKit.Container`](cloudkit.container.md) class and implement the listener to handle the push notifications.

```javascript
myContainer.addNotificationListener(function(notification) {
    console.log(notification);
});
```

For details on the [`CloudKit.Notification`](cloudkit.notification.md) object passed to the listener, read [`CloudKit.Notification`](cloudkit.notification.md).

Registering for Subscription Push Notifications

Saving subscriptions to the database doesn’t automatically configure your web app to receive notifications when a subscription fires. CloudKit uses the Apple Push Notification service (APNs) to send notifications, so your web app needs to register for push notifications to receive them.

To receive push notifications when a subscription fires, use the [`registerForNotifications`](cloudkit.container/registerfornotifications.md) method in the [`CloudKit.Container`](cloudkit.container.md) class.

```javascript
var myContainer = CloudKit.getDefaultContainer();
myContainer.registerForNotifications();
```

## Parameters

- `subscriptions`: Possible values are:

## See Also

- [fetchSubscriptions](cloudkit.database/fetchsubscriptions.md)
  Fetches one or more subscriptions.
- [fetchAllSubscriptions](cloudkit.database/fetchallsubscriptions.md)
  Fetches all subscriptions in the schema.
- [deleteSubscriptions](cloudkit.database/deletesubscriptions.md)
  Deletes one or more subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/savesubscriptions)*