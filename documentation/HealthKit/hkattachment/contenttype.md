# contentType

**Framework**: HealthKit  
**Kind**: property

The type of data stored in the attached file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var contentType: UTType { get }
```

## See Also

- [var name: String](hkattachment/name.md)
  The name of the attached file.
- [var identifier: UUID](hkattachment/identifier.md)
  The universally unique identifier for the attached file.
- [var size: Int](hkattachment/size.md)
  The attachment’s size (in bytes).
- [var creationDate: Date](hkattachment/creationdate.md)
  The attachment’s creation date.
- [var metadata: [String : Any]?](hkattachment/metadata.md)
  Additional data associated with the attachment in the HealthKit store.
- [HKAttachment.AsyncBytes](hkattachment/asyncbytes.md)
  An asynchronous sequence that returns the attached file as a series of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachment/contenttype)*