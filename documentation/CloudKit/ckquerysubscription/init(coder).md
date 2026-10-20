# init(coder:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a query-based subscription from a serialized instance.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Parameters

- `aDecoder`: The coder for decoding the serialized query subscription.

## See Also

### Creating a Subscription
- [convenience init(recordType: CKRecord.RecordType, predicate: NSPredicate, subscriptionID: CKSubscription.ID, options: CKQuerySubscription.Options)](./init%28recordtype,predicate,subscriptionid,options%29.md)
  Creates a named query-based subscription that queries records of a specific type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/init(coder:))*