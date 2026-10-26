# setObject:forKeyedSubscript:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Stores an object in the record using the specified key.

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
- (void) setObject:(id<CKRecordValue>) object forKeyedSubscript:(CKRecordFieldKey) key;
```

#### Discussion

> ❗ **Important**: Don’t call this method directly. The presence of this method is necessary to support subscripting syntax for record objects.

## Parameters

- `object`: The object to store using the specified key. It must be one of the data types in [Supported Data Types](../ckrecord.md#Supported-Data-Types). You receive an error if you use a data type that CloudKit doesn’t support. If you specify `nil`, CloudKit removes any object that the record associates with the key.
- `key`: The key to associate with `object`. Use this key to retrieve the value later. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces. Avoid using a key that matches the name of any property of `CKRecord`.

## See Also

### Accessing the Record’s Fields
- [- objectForKey:](./objectforkey_.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29-51whk.md)
  Returns the object that the record stores for the specified key.
- [- setObject:forKey:](./setobject_forkey_.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/setobject:forkeyedsubscript:)*