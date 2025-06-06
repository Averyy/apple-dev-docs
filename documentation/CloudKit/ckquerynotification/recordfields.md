# recordFields

**Framework**: CloudKit  
**Kind**: property

A dictionary of fields that have changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var recordFields: [String : Any]? { get }
```

#### Discussion

For updated and created records, this property contains the subscription’s desired keys. When you configure the notification info of a subscription, you specify the names of one or more fields in the [`desiredKeys`](cksubscription/notificationinfo-swift.class/desiredkeys.md) property. When a push notification triggers, CloudKit retrieves the values for each of those keys from the record and includes them in the notification’s payload.

For query notifications that you fetch from a container, all keys and values are present. For query notifications that you create from push notifications, one or more keys and values may be missing. Push notification payloads have a size limit, and CloudKit can exclude record fields when a payload exceeds that limit. For information about the order, see the overview of this class.

## See Also

- [var recordID: CKRecord.ID?](ckquerynotification/recordid.md)
  The ID of the record that CloudKit creates, updates, or deletes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerynotification/recordfields)*