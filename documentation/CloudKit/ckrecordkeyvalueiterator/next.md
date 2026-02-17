# next()

**Framework**: CloudKit  
**Kind**: method

Advances the iterator and returns the next key-value pair from the record.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
mutating func next() -> (CKRecord.FieldKey, any CKRecordValueProtocol)?
```

#### Return Value

The next key-value pair from the record, or `nil` if there are no more keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvalueiterator/next())*