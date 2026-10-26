# subscript(_:)

**Framework**: CloudKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the object that the record stores for the specified key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
subscript(key: String) -> (any __CKRecordObjCValue)? { get set }
```

```objc
- (id<CKRecordValue>) objectForKeyedSubscript:(CKRecordFieldKey) key;
```

#### Return Value

The object for the specified key, or `nil` if no such key exists in the record.

#### Discussion

> ❗ **Important**: Don’t call this method directly. The presence of this method is necessary to support subscripting syntax for record objects.

## Parameters

- `key`: The string that identifies a field in the record. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.

## See Also

### Accessing the Record’s Fields
- [func object(forKey: CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](./object%28forkey%29.md)
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
- [- objectForKey:](./objectforkey_.md)
  Returns the object that the record stores for the specified key.
- [- setObject:forKey:](./setobject_forkey_.md)
  Stores an object in the record using the specified key.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Stores an object in the record using the specified key.
- [- allKeys](./allkeys.md)
  Returns an array of the record’s keys.
- [- changedKeys](./changedkeys.md)
  Returns an array of keys with recent changes to their values.
- [CKRecordCreationDateKey](../ckrecordcreationdatekey.md)
  A key constant that a record uses for its CKRecord.creationDate.
- [CKRecordCreatorUserRecordIDKey](../ckrecordcreatoruserrecordidkey.md)
  A key constant that a record uses for its CKRecord.creatorUserRecordID.
- [CKRecordLastModifiedUserRecordIDKey](../ckrecordlastmodifieduserrecordidkey.md)
  A key constant that a record uses for its CKRecord.lastModifiedUserRecordID.
- [CKRecordModificationDateKey](../ckrecordmodificationdatekey.md)
  A key constant that a record uses for its CKRecord.modificationDate.
- [CKRecordRecordIDKey](../ckrecordrecordidkey.md)
  A key constant that a record uses for its CKRecord.recordID.
- [CKRecordParentKey](../ckrecordparentkey-2kx8l.md)
  The key constant that a record uses for its CKRecord.parent.
- [CKRecordShareKey](../ckrecordsharekey-rrat.md)
  The key constant that a record uses for its CKRecord.share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/subscript(_:)-51whk)*