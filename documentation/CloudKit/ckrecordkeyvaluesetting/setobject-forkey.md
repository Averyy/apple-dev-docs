# setObject(_:forKey:)

**Framework**: CloudKit  
**Kind**: method  
**Required**: Yes

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

```swift
func setObject(_ object: (any __CKRecordObjCValue)?, forKey key: String)
```

## Parameters

- `object`: The object to store using the specified key. It must be one of the data types in  . You receive an error if you use a data type that CloudKit doesn’t support. If you specify  , CloudKit removes any object that the record associates with the key.
- `key`: The key to associate with  . Use this key to retrieve the value later. A key must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces. Avoid using a key that matches the name of any property of  .

## See Also

- [func object(forKey: String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/object(forkey:).md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/subscript(_:).md)
  Returns the object that the record stores for the specified key.
- [func allKeys() -> [String]](ckrecordkeyvaluesetting/allkeys.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [String]](ckrecordkeyvaluesetting/changedkeys.md)
  Returns an array of keys with recent changes to their values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/setobject(_:forkey:))*