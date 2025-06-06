# clientRecord

**Framework**: CloudKit  
**Kind**: property

The local version of the record that includes any changes.

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
var clientRecord: CKRecord? { get }
```

#### Discussion

This property’s value is available only when the error’s `code` is [`serverRecordChanged`](ckerror/serverrecordchanged.md), which indicates the server’s record is newer than the version you try to save. Use this property’s value, along with those of [`ancestorRecord`](ckerror/ancestorrecord.md) and [`serverRecord`](ckerror/serverrecord.md), to resolve the conflict.

The error’s `userInfo` dictionary contains the same value as this property. you can access it using the [`CKRecordChangedErrorClientRecordKey`](ckrecordchangederrorclientrecordkey.md) key.

## See Also

- [var ancestorRecord: CKRecord?](ckerror/ancestorrecord.md)
  The original version of the record.
- [var serverRecord: CKRecord?](ckerror/serverrecord.md)
  The server’s version of the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/clientrecord)*