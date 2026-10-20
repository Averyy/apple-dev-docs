# init(recordType:predicate:options:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.12
- tvOS 10.0+ - Deprecated in 10.0
- visionOS - Deprecated
- watchOS 6.0+ - Deprecated in 6.0
- Swift 4.2+

> **Deprecated**: Provide an explicit CKSubscription.ID at CKSubscription-init time

## Declaration

```swift
convenience init(recordType: CKRecord.RecordType, predicate: NSPredicate, options querySubscriptionOptions: CKQuerySubscription.Options = [.firesOnRecordCreation, .firesOnRecordUpdate, .firesOnRecordDeletion])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/init(recordtype:predicate:options:))*