# RCSFileTransferMetadata

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains metadata about an RCS file transfer.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct RCSFileTransferMetadata
```

## Topics

### Accessing file metadata
- [let url: URL](rcsfiletransfermetadata/url.md)
  The URL for the file.
- [let fileName: String?](rcsfiletransfermetadata/filename.md)
  The original name of file.
- [let fileSize: Int](rcsfiletransfermetadata/filesize.md)
  The size of the file in bytes.
- [let contentType: UTType?](rcsfiletransfermetadata/contenttype.md)
  The content type of the file.
- [let expirationDate: Date](rcsfiletransfermetadata/expirationdate.md)
  The expiration date of the file.
- [var playbackLength: Duration?](rcsfiletransfermetadata/playbacklength.md)
  Playback length of RCS Recorded Audio Message (RRAM).
### Working with file disposition
- [var disposition: RCSFileTransferMetadata.Disposition?](rcsfiletransfermetadata/disposition-swift.property.md)
  The disposition of the file, indicating how a recipient needs to handle the file.
- [RCSFileTransferMetadata.Disposition](rcsfiletransfermetadata/disposition-swift.enum.md)
  An enumeration that represents the disposition of the file, indicating how a receiving app should handle it.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct RCSGroupContext](rcsgroupcontext.md)
  Structure containing information about a message’s group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsfiletransfermetadata)*