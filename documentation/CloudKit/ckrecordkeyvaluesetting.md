# CKRecordKeyValueSetting

**Framework**: CloudKit  
**Kind**: protocol

A protocol for managing the key-value pairs of a CloudKit record.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol CKRecordKeyValueSetting : NSObjectProtocol
```

## Topics

### Accessing a Record’s Fields
- [func object(forKey: String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/object(forkey:).md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/subscript(_:).md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](ckrecordkeyvaluesetting/setobject(_:forkey:).md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [String]](ckrecordkeyvaluesetting/allkeys.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [String]](ckrecordkeyvaluesetting/changedkeys.md)
  Returns an array of keys with recent changes to their values.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [CKRecord](ckrecord.md)
- [CKShare](ckshare.md)

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
- [struct CKRecordKeyValueIterator](ckrecordkeyvalueiterator.md)
  An iterator of the record’s key-value pairs.
- [protocol CKRecordValueProtocol](ckrecordvalueprotocol.md)
  A description of a CloudKit record value.
- [typealias CKRecordValue](ckrecordvalue-swift.typealias.md)
  A data type for objects that CloudKit stores on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting)*