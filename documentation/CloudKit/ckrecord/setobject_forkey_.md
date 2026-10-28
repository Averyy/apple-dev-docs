# setObject:forKey:

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
- (void) setObject:(id<CKRecordValue>) object forKey:(CKRecordFieldKey) key;
```

## Discussion

If the specified key already exists in the record, CloudKit deletes its previous value and replaces it with the one in the `object` parameter. This change affects only the local copy of the record. You must save the record to the server again before the change becomes available to other clients.

If the type of the `object` parameter differs from the type of the object that’s on the server, you encounter an error when you attempt to save this record to the server. For example, if the current value is an [`NSString`](../../Foundation/nsstring.md) object, you receive an error if you change the value to an [`NSNumber`](../../Foundation/nsnumber.md) object and save the record.

You access the fields of a `CKRecord` object the same way you access key-value pairs in a dictionary. The `CKRecord` class defines the [`objectForKey:`](./objectforkey_.md) and [`setObject:forKey:`](./setobject_forkey_.md) methods for getting and setting values. It also supports dictionary index notation. The following example shows how to use both techniques to set a `firstName` field and get a `lastName` field from a record:

```objc
// Equivalent ways to set a value.
[myRecord setObject:[NSDate date] forKey:@"hiredAt"];
myRecord[@"hiredAt"] = [NSDate date];
```

## Parameters

- `object`: The object to store using the specified key. The value you provide must be an instance of one the data types in [Supported Data Types](../ckrecord.md#Supported-Data-Types). You receive an error if you use a data type that CloudKit doesn’t support. If you specify `nil`, CloudKit removes any object that the record associates with the key.
- `key`: The key to associate with `object`. Use this key to retrieve the value later. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces. Avoid using a key that matches the name of any property of `CKRecord`.

## See Also

### Accessing the Record’s Fields
- [- objectForKey:](./objectforkey_.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29-51whk.md)
  Returns the object that the record stores for the specified key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/setobject:forkey:)*