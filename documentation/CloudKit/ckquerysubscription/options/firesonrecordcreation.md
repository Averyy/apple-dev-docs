# firesOnRecordCreation

**Framework**: CloudKit  
**Kind**: property  
**Role**: Type Property

An option that instructs CloudKit to send a push notification when it creates a record that matches a subscription’s criteria.

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
static var firesOnRecordCreation: CKQuerySubscription.Options { get }
```

```c
CKQuerySubscriptionOptionsFiresOnRecordCreation
```

## See Also

### Accessing Subscription Options
- [static var firesOnRecordDeletion: CKQuerySubscription.Options](./firesonrecorddeletion.md)
  An option that instructs CloudKit to send a push notification when it deletes a record that matches a subscription’s criteria.
- [static var firesOnRecordUpdate: CKQuerySubscription.Options](./firesonrecordupdate.md)
  An option that instructs CloudKit to send a push notification when it modifies a record that matches a subscription’s criteria.
- [static var firesOnce: CKQuerySubscription.Options](./firesonce.md)
  An option that instructs CloudKit to send a push notification only once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options/firesonrecordcreation)*