# CKRecordKeyValueIterator

**Framework**: CloudKit  
**Kind**: struct

An iterator of the record’s key-value pairs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
struct CKRecordKeyValueIterator
```

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)

## See Also

- [func object(forKey: CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](ckrecord/object(forkey:).md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](ckrecord/subscript(_:)-51whk.md)
  Returns the object that the record stores for the specified key.
- [subscript(CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](ckrecord/subscript(_:)-4g91i.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: CKRecord.FieldKey)](ckrecord/setobject(_:forkey:).md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [CKRecord.FieldKey]](ckrecord/allkeys.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [CKRecord.FieldKey]](ckrecord/changedkeys.md)
  Returns an array of keys with recent changes to their values.
- [protocol CKRecordValueProtocol](ckrecordvalueprotocol.md)
  A description of a CloudKit record value.
- [protocol CKRecordKeyValueSetting](ckrecordkeyvaluesetting.md)
  A protocol for managing the key-value pairs of a CloudKit record.
- [typealias CKRecordValue](ckrecordvalue-swift.typealias.md)
  A data type for objects that CloudKit stores on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvalueiterator)*