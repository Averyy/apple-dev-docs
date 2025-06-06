# serverRecord

**Framework**: CloudKit  
**Kind**: property

The server’s version of the record.

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
var serverRecord: CKRecord? { get }
```

#### Discussion

This property’s value is available only when the error’s `code` is [`serverRecordChanged`](ckerror/serverrecordchanged.md), which indicates the server’s record is newer than the version you try to save. Use this property’s value, along with those of [`ancestorRecord`](ckerror/ancestorrecord.md) and [`clientRecord`](ckerror/clientrecord.md), to resolve the conflict.

The error’s `userInfo` dictionary contains the same value as this property. You can access it using the [`CKRecordChangedErrorServerRecordKey`](ckrecordchangederrorserverrecordkey.md) key.

## See Also

- [var ancestorRecord: CKRecord?](ckerror/ancestorrecord.md)
  The original version of the record.
- [var clientRecord: CKRecord?](ckerror/clientrecord.md)
  The local version of the record that includes any changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/serverrecord)*