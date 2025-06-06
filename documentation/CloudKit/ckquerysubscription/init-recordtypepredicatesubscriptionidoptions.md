# init(recordType:predicate:subscriptionID:options:)

**Framework**: CloudKit  
**Kind**: init

Creates a named query-based subscription that queries records of a specific type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
convenience init(recordType: CKRecord.RecordType, predicate: NSPredicate, subscriptionID: CKSubscription.ID, options querySubscriptionOptions: CKQuerySubscription.Options = [.firesOnRecordCreation, .firesOnRecordUpdate, .firesOnRecordDeletion])
```

#### Discussion

The subscription that this method returns is a query-based subscription with a scope that includes all of the user’s record zones. When CloudKit modifies a record that matches the specified type and predicate, it uses `querySubscriptionOptions` to determine whether to send a push notification.

## Parameters

- `recordType`: The record’s type. You’re responsible for defining your app’s record types.
- `predicate`: The predicate that identifies the records for inclusion in the subscription. For information about the operators that predicates support, see the discussion in  .
- `subscriptionID`: The subscription’s name. It must be unique in the target database, and must not be an empty string.
- `querySubscriptionOptions`: A bitmask of configuration options. See   for more information.

## See Also

- [init(coder: NSCoder)](ckquerysubscription/init(coder:).md)
  Creates a query-based subscription from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/init(recordtype:predicate:subscriptionid:options:))*