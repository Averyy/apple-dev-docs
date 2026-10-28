# object(forKey:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Returns the object that the record stores for the specified key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
func object(forKey key: CKRecord.FieldKey) -> (any __CKRecordObjCValue)?
```

## Return Value

The object for the specified key, or `nil` if no such key exists in the record.

## Discussion

New records don’t contain any keys or values. Values are always one of the data types in [Supported Data Types](../ckrecord.md#Supported-Data-Types).

You access the fields of a `CKRecord` object the same way you access key-value pairs in a dictionary. The `CKRecord` class defines the [`object(forKey:)`](./object%28forkey%29.md) and [`setObject(_:forKey:)`](./setobject%28_,forkey%29.md) methods for getting and setting values. It also supports dictionary index notation. The following example shows how to use both techniques to set a `firstName` field and retrieve a `lastName` field from a record:

```swift
// Equivalent ways to get a value.
var hiredAt = record.object(forKey: "hiredAt")
hiredAt = record["hiredAt"]
```

## Parameters

- `key`: The string that identifies a field in the record. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.

## See Also

### Accessing the Record’s Fields
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
- [func makeIterator() -> CKRecordKeyValueIterator](./makeiterator%28%29.md)
  Returns an iterator of the record’s key-value pairs.
- [struct CKRecordKeyValueIterator](../ckrecordkeyvalueiterator.md)
  An iterator of the record’s key-value pairs.
- [protocol CKRecordValueProtocol](../ckrecordvalueprotocol.md)
  A description of a CloudKit record value.
- [protocol CKRecordKeyValueSetting](../ckrecordkeyvaluesetting.md)
  A protocol for managing the key-value pairs of a CloudKit record.
- [typealias CKRecordValue](../ckrecordvalue-swift.typealias.md)
  A data type for objects that CloudKit stores on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/object(forkey:))*