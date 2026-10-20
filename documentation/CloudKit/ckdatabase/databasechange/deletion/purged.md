# purged

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user deleted the record zone when managing their iCloud storage.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 15.0+ - Deprecated in 17.0
- visionOS - Deprecated
- watchOS 8.0+ - Deprecated in 10.0

> **Deprecated**: now surfaced as Reason.purged

## Declaration

```swift
var purged: Bool { get }
```

## See Also

### Identifying the Deleted Record Zone
- [var zoneID: CKRecordZone.ID](./zoneid.md)
  The identifier of the deleted record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/databasechange/deletion/purged)*