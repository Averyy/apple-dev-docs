# allKeys()

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (NSArray<NSString *> *) allKeys;
```

#### Return Value

An array of keys, or an empty array if the record doesn’t contain any keys.

## See Also

### Accessing a Record’s Fields
- [func object(forKey: String) -> (any __CKRecordObjCValue)?](./object%28forkey%29.md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](./subscript%28_%29.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: String)](./setobject%28_,forkey%29.md)
  Stores an object in the record using the specified key.
- [func changedKeys() -> [String]](./changedkeys%28%29.md)
  Returns an array of keys with recent changes to their values.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Stores an object in the record using the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/allkeys())*