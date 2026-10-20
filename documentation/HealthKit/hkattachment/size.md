# size

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The attachment’s size (in bytes).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var size: Int { get }
```

```objc
@property (assign, readonly) NSInteger size;
```

## See Also

### Accessing attachment data
- [var name: String](./name.md)
  The name of the attached file.
- [var identifier: UUID](./identifier.md)
  The universally unique identifier for the attached file.
- [var contentType: UTType](./contenttype.md)
  The type of data stored in the attached file.
- [var creationDate: Date](./creationdate.md)
  The attachment’s creation date.
- [var metadata: [String : Any]?](./metadata.md)
  Additional data associated with the attachment in the HealthKit store.
- [HKAttachment.AsyncBytes](./asyncbytes.md)
  An asynchronous sequence that returns the attached file as a series of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachment/size)*