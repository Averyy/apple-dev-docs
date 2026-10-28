# changedKeys

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of keys with recent changes to their values.

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
- (NSArray<NSString *> *) changedKeys;
```

## Return Value

An array of keys with changed values since downloading or saving the record. If there aren’t any changed keys, this method returns an empty array.

## See Also

### Accessing the Record’s Fields
- [- objectForKey:](./objectforkey_.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29-51whk.md)
  Returns the object that the record stores for the specified key.
- [- setObject:forKey:](./setobject_forkey_.md)
  Stores an object in the record using the specified key.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Stores an object in the record using the specified key.
- [- allKeys](./allkeys.md)
  Returns an array of the record’s keys.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/changedkeys)*