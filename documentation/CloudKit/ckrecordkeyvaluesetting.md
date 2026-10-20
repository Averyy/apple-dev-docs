# CKRecordKeyValueSetting

**Framework**: CloudKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CKRecordKeyValueSetting <NSObject>
```

## Topics

### Accessing a Record’s Fields
- [func object(forKey: String) -> (any __CKRecordObjCValue)?](./ckrecordkeyvaluesetting/object%28forkey%29.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./ckrecordkeyvaluesetting/subscript%28_%29.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](./ckrecordkeyvaluesetting/setobject%28_,forkey%29.md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [String]](./ckrecordkeyvaluesetting/allkeys%28%29.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [String]](./ckrecordkeyvaluesetting/changedkeys%28%29.md)
  Returns an array of keys with recent changes to their values.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [CKRecord](./ckrecord.md)
- [CKShare](./ckshare.md)

## See Also

### Accessing the Record’s Fields
- [func object(forKey: CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](./ckrecord/object%28forkey%29.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./ckrecord/subscript%28_%29-51whk.md)
  Returns the object that the record stores for the specified key.
- [subscript(CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](./ckrecord/subscript%28_%29-4g91i.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: CKRecord.FieldKey)](./ckrecord/setobject%28_,forkey%29.md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [CKRecord.FieldKey]](./ckrecord/allkeys%28%29.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [CKRecord.FieldKey]](./ckrecord/changedkeys%28%29.md)
  Returns an array of keys with recent changes to their values.
- [func makeIterator() -> CKRecordKeyValueIterator](./ckrecord/makeiterator%28%29.md)
  Returns an iterator of the record’s key-value pairs.
- [struct CKRecordKeyValueIterator](./ckrecordkeyvalueiterator.md)
  An iterator of the record’s key-value pairs.
- [protocol CKRecordValueProtocol](./ckrecordvalueprotocol.md)
  A description of a CloudKit record value.
- [typealias CKRecordValue](./ckrecordvalue-swift.typealias.md)
  A data type for objects that CloudKit stores on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting)*