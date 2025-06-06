# firesOnce

**Framework**: CloudKit  
**Kind**: property

An option that instructs CloudKit to send a push notification only once.

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
static var firesOnce: CKQuerySubscription.Options { get }
```

#### Discussion

You combine this option with one or more of the other subscription options. This option applies only to query-based subscriptions. CloudKit deletes the subscription after it sends the push notification. If you want to generate subsequent push notifications using the same criteria, create and save a new subscription.

## See Also

- [static var firesOnRecordCreation: CKQuerySubscription.Options](ckquerysubscription/options/firesonrecordcreation.md)
  An option that instructs CloudKit to send a push notification when it creates a record that matches a subscription’s criteria.
- [static var firesOnRecordDeletion: CKQuerySubscription.Options](ckquerysubscription/options/firesonrecorddeletion.md)
  An option that instructs CloudKit to send a push notification when it deletes a record that matches a subscription’s criteria.
- [static var firesOnRecordUpdate: CKQuerySubscription.Options](ckquerysubscription/options/firesonrecordupdate.md)
  An option that instructs CloudKit to send a push notification when it modifies a record that matches a subscription’s criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/options/firesonce)*