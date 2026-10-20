# CKQuerySubscription.Options

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum CKQuerySubscriptionOptions : NSUInteger;
```

## Topics

### Creating Query Subscription Options
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
  Creates a query subscription option using the specified raw value.
### Accessing Subscription Options
- [static var firesOnRecordCreation: CKQuerySubscription.Options](./options/firesonrecordcreation.md)
  An option that instructs CloudKit to send a push notification when it creates a record that matches a subscription’s criteria.
- [static var firesOnRecordDeletion: CKQuerySubscription.Options](./options/firesonrecorddeletion.md)
  An option that instructs CloudKit to send a push notification when it deletes a record that matches a subscription’s criteria.
- [static var firesOnRecordUpdate: CKQuerySubscription.Options](./options/firesonrecordupdate.md)
  An option that instructs CloudKit to send a push notification when it modifies a record that matches a subscription’s criteria.
- [static var firesOnce: CKQuerySubscription.Options](./options/firesonce.md)
  An option that instructs CloudKit to send a push notification only once.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Accessing the Subscription Search Parameters
- [var predicate: NSPredicate](./predicate.md)
  The matching criteria to apply to records.
- [var querySubscriptionOptions: CKQuerySubscription.Options](./querysubscriptionoptions.md)
  Options that define the behavior of the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options)*