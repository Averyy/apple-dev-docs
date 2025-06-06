# metadata

**Framework**: HealthKit  
**Kind**: property

Additional data associated with the attachment in the HealthKit store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var metadata: [String : Any]? { get }
```

#### Discussion

The metadata dictionary contains extra information describing this object. The dictionary’s keys are all strings. The values can be strings, numbers, or dates. For a complete list of predefined metadata keys, see [`Metadata Keys`](metadata-keys.md).

Using predefined keys helps facilitate sharing data between apps; however, you’re also encouraged to create your own, custom keys as needed to extend a HealthKit object’s capabilities.

## See Also

- [var name: String](hkattachment/name.md)
  The name of the attached file.
- [var identifier: UUID](hkattachment/identifier.md)
  The universally unique identifier for the attached file.
- [var contentType: UTType](hkattachment/contenttype.md)
  The type of data stored in the attached file.
- [var size: Int](hkattachment/size.md)
  The attachment’s size (in bytes).
- [var creationDate: Date](hkattachment/creationdate.md)
  The attachment’s creation date.
- [HKAttachment.AsyncBytes](hkattachment/asyncbytes.md)
  An asynchronous sequence that returns the attached file as a series of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachment/metadata)*