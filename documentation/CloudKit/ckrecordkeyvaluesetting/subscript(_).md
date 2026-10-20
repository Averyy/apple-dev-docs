# subscript(_:)

**Framework**: CloudKit  
**Kind**: subscript  
**Role**: Instance Subscript  
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
subscript(key: String) -> (any __CKRecordObjCValue)? { get set }
```

```objc
- (id<CKRecordValue>) objectForKeyedSubscript:(CKRecordFieldKey) key;
```

#### Return Value

The object for the specified key, or `nil` if no such key exists in the record.

## Parameters

- `key`: The string that identifies a field in the record. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.

## Default Implementations

### CKRecordKeyValueSetting Implementations
- [subscript(CKRecord.FieldKey) -> (any CKRecordValueProtocol)?](./subscript%28_%29-2uqmn.md)
  Accesses the value for the specified key in the record.
- [subscript<T>(CKRecord.FieldKey) -> T?](./subscript%28_%29-4f12u.md)
  Accesses the value for the specified key in the record.

## See Also

### Accessing a Record’s Fields
- [func object(forKey: String) -> (any __CKRecordObjCValue)?](./object%28forkey%29.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](./setobject%28_,forkey%29.md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [String]](./allkeys%28%29.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [String]](./changedkeys%28%29.md)
  Returns an array of keys with recent changes to their values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/subscript(_:))*