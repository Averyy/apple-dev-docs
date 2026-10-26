# setObject:forKeyedSubscript:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Stores an object in the record using the specified key.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
- (void) setObject:(id<CKRecordValue>) object forKeyedSubscript:(CKRecordFieldKey) key;
```

## Parameters

- `object`: The object to store using the specified key. It must be one of the data types in [Supported Data Types](../ckrecord.md#Supported-Data-Types). You receive an error if you use a data type that CloudKit doesn’t support. If you specify `nil`, CloudKit removes any object that the record associates with the key.
- `key`: The key to associate with `object`. Use this key to retrieve the value later. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces. Avoid using a key that matches the name of any property of `CKRecord`.

## See Also

### Accessing a Record’s Fields
- [func object(forKey: String) -> (any __CKRecordObjCValue)?](./object%28forkey%29.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](./setobject%28_,forkey%29.md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [String]](./allkeys%28%29.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [String]](./changedkeys%28%29.md)
  Returns an array of keys with recent changes to their values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/setobject:forkeyedsubscript:)*