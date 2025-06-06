# CKQuerySubscription.Options

**Framework**: CloudKit  
**Kind**: struct

Configuration options for a query subscription.

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
struct Options
```

## Topics

### Creating Query Subscription Options
- [init(rawValue: UInt)](ckquerysubscription/options/init(rawvalue:).md)
  Creates a query subscription option using the specified raw value.
### Accessing Subscription Options
- [static var firesOnRecordCreation: CKQuerySubscription.Options](ckquerysubscription/options/firesonrecordcreation.md)
  An option that instructs CloudKit to send a push notification when it creates a record that matches a subscription’s criteria.
- [static var firesOnRecordDeletion: CKQuerySubscription.Options](ckquerysubscription/options/firesonrecorddeletion.md)
  An option that instructs CloudKit to send a push notification when it deletes a record that matches a subscription’s criteria.
- [static var firesOnRecordUpdate: CKQuerySubscription.Options](ckquerysubscription/options/firesonrecordupdate.md)
  An option that instructs CloudKit to send a push notification when it modifies a record that matches a subscription’s criteria.
- [static var firesOnce: CKQuerySubscription.Options](ckquerysubscription/options/firesonce.md)
  An option that instructs CloudKit to send a push notification only once.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var predicate: NSPredicate](ckquerysubscription/predicate.md)
  The matching criteria to apply to records.
- [var querySubscriptionOptions: CKQuerySubscription.Options](ckquerysubscription/querysubscriptionoptions.md)
  Options that define the behavior of the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options)*