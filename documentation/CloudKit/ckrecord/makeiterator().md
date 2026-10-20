# makeIterator()

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Returns an iterator of the record’s key-value pairs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS
- watchOS 3.0+

## Declaration

```swift
func makeIterator() -> CKRecordKeyValueIterator
```

## See Also

### Accessing the Record’s Fields
- [func object(forKey: CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](./object%28forkey%29.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29-51whk.md)
  Returns the object that the record stores for the specified key.
- [subscript(CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](./subscript%28_%29-4g91i.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: CKRecord.FieldKey)](./setobject%28_,forkey%29.md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [CKRecord.FieldKey]](./allkeys%28%29.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [CKRecord.FieldKey]](./changedkeys%28%29.md)
  Returns an array of keys with recent changes to their values.
- [struct CKRecordKeyValueIterator](../ckrecordkeyvalueiterator.md)
  An iterator of the record’s key-value pairs.
- [protocol CKRecordValueProtocol](../ckrecordvalueprotocol.md)
  A description of a CloudKit record value.
- [protocol CKRecordKeyValueSetting](../ckrecordkeyvaluesetting.md)
  A protocol for managing the key-value pairs of a CloudKit record.
- [typealias CKRecordValue](../ckrecordvalue-swift.typealias.md)
  A data type for objects that CloudKit stores on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/makeiterator())*