# objectIDNotification()

**Framework**: Core Data  
**Kind**: method

Obtains a notification for use in merging the transaction’s changes into a managed object context.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func objectIDNotification() -> Notification
```

## Mentions

- [Consuming relevant store changes](consuming-relevant-store-changes.md)

#### Return Value

An `NSManagedObjectContextDidSaveObjectIDsNotification` notification.

#### Discussion

To merge the relevant changes into your view context, first obtain a notification by calling `objectIDNotification()` on the transaction. Then, pass the notification to [`mergeChanges(fromContextDidSave:)`](nsmanagedobjectcontext/mergechanges(fromcontextdidsave:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/objectidnotification())*