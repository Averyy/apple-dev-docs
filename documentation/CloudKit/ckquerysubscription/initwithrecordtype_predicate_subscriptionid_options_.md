# initWithRecordType:predicate:subscriptionID:options:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a named query-based subscription that queries records of a specific type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (instancetype) initWithRecordType:(CKRecordType) recordType predicate:(NSPredicate *) predicate subscriptionID:(CKSubscriptionID) subscriptionID options:(CKQuerySubscriptionOptions) querySubscriptionOptions;
```

## Discussion

The subscription that this method returns is a query-based subscription with a scope that includes all of the user’s record zones. When CloudKit modifies a record that matches the specified type and predicate, it uses `querySubscriptionOptions` to determine whether to send a push notification.

## Parameters

- `recordType`: The record’s type. You’re responsible for defining your app’s record types. This parameter must not be `nil` or an empty string.
- `predicate`: The predicate that identifies the records for inclusion in the subscription. This parameter must not be `nil`. For information about the operators that predicates support, see the discussion in [`CKQuery`](../ckquery.md).
- `subscriptionID`: The subscription’s name. You should provide a value that is unique in the target database, and you may not provide `nil` or an empty string.
- `querySubscriptionOptions`: A bitmask of configuration options. See [`CKQuerySubscription.Options`](./options.md) for more information.

## See Also

### Creating a Subscription
- [- initWithRecordType:predicate:options:](./initwithrecordtype_predicate_options_.md)
  Creates a query-based subscription that queries records of a specific type.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a query-based subscription from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/initwithrecordtype:predicate:subscriptionid:options:)*