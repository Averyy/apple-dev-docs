# objectForKey:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id<CKRecordValue>) objectForKey:(CKRecordFieldKey) key;
```

## Return Value

The object for the specified key, or `nil` if no such key exists in the record.

## Discussion

New records don’t contain any keys or values. Values are always one of the data types in [Supported Data Types](../ckrecord.md#Supported-Data-Types).

You access the fields of a `CKRecord` object the same way you access key-value pairs in a dictionary. The `CKRecord` class defines the [`objectForKey:`](./objectforkey_.md) and [`setObject:forKey:`](./setobject_forkey_.md) methods for getting and setting values. It also supports dictionary index notation. The following example shows how to use both techniques to set a `firstName` field and retrieve a `lastName` field from a record:

```objc
// Equivalent ways to get a value.
id value = [myRecord objectForKey:@"hiredAt"];
value = myRecord[@"hiredAt"];
```

## Parameters

- `key`: The string that identifies a field in the record. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.

## See Also

### Accessing the Record’s Fields
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29-51whk.md)
  Returns the object that the record stores for the specified key.
- [- setObject:forKey:](./setobject_forkey_.md)
  Stores an object in the record using the specified key.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Stores an object in the record using the specified key.
- [- allKeys](./allkeys.md)
  Returns an array of the record’s keys.
- [- changedKeys](./changedkeys.md)
  Returns an array of keys with recent changes to their values.
- [protocol CKRecordKeyValueSetting](../ckrecordkeyvaluesetting.md)
  A protocol for managing the key-value pairs of a CloudKit record.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/objectforkey:)*