# allKeys()

**Framework**: CloudKit  
**Kind**: method  
**Required**: Yes

Returns an array of the record’s keys.

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
func allKeys() -> [String]
```

#### Return Value

An array of keys, or an empty array if the record doesn’t contain any keys.

## See Also

- [func object(forKey: String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/object(forkey:).md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/subscript(_:).md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](ckrecordkeyvaluesetting/setobject(_:forkey:).md)
  Stores an object in the record using the specified key.
- [func changedKeys() -> [String]](ckrecordkeyvaluesetting/changedkeys.md)
  Returns an array of keys with recent changes to their values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/allkeys())*