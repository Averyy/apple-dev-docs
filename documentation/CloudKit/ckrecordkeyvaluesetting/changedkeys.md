# changedKeys()

**Framework**: CloudKit  
**Kind**: method  
**Required**: Yes

Returns an array of keys with recent changes to their values.

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
func changedKeys() -> [String]
```

#### Return Value

An array of keys with changed values since downloading or saving the record. If there aren’t any changed keys, this method returns an empty array.

## See Also

- [func object(forKey: String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/object(forkey:).md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](ckrecordkeyvaluesetting/subscript(_:).md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](ckrecordkeyvaluesetting/setobject(_:forkey:).md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [String]](ckrecordkeyvaluesetting/allkeys.md)
  Returns an array of the record’s keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/changedkeys())*