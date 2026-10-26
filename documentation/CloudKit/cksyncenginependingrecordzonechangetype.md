# CKSyncEnginePendingRecordZoneChangeType

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

A type of change in a record zone that needs to be sent to the server.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum CKSyncEnginePendingRecordZoneChangeType
```

```c
enum CKSyncEnginePendingRecordZoneChangeType : NSInteger;
```

## Topics

### Enumeration Cases
- [CKSyncEnginePendingRecordZoneChangeType.deleteRecord](./cksyncenginependingrecordzonechangetype/deleterecord.md)
- [CKSyncEnginePendingRecordZoneChangeType.saveRecord](./cksyncenginependingrecordzonechangetype/saverecord.md)
### Initializers
- [init?(rawValue: Int)](./cksyncenginependingrecordzonechangetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing the modified record
- [recordID](./cksyncenginependingrecordzonechange/recordid.md)
  The identifier of the modified record.
- [type](./cksyncenginependingrecordzonechange/type.md)
  The type of change to make.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginependingrecordzonechangetype)*