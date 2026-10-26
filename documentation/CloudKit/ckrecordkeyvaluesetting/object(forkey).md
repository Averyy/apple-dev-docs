# object(forKey:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the object that the record stores for the specified key.

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
func object(forKey key: String) -> (any __CKRecordObjCValue)?
```

```objc
- (id<CKRecordValue>) objectForKey:(CKRecordFieldKey) key;
```

#### Return Value

The object for the specified key, or `nil` if no such key exists in the record.

## Parameters

- `key`: The string that identifies a field in the record. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.

## See Also

### Accessing a Record’s Fields
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](./setobject%28_,forkey%29.md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [String]](./allkeys%28%29.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [String]](./changedkeys%28%29.md)
  Returns an array of keys with recent changes to their values.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Stores an object in the record using the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/object(forkey:))*