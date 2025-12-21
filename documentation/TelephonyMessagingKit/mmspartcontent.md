# MMSPartContent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that defines custom headers within MMS content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct MMSPartContent
```

## Topics

### Creating a content part
- [init(data: Data, contentType: UTType?, contentID: String, disposition: MMSPartContent.MMSDispositionType, fileName: String)](mmspartcontent/init(data:contenttype:contentid:disposition:filename:).md)
  Creates an MMS part with the provided values.
### Accessing part properties
- [var data: Data](mmspartcontent/data.md)
  The raw data used for the MMS content part.
- [var disposition: MMSPartContent.MMSDispositionType](mmspartcontent/disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [MMSPartContent.MMSDispositionType](mmspartcontent/mmsdispositiontype.md)
  A structure that defines the disposition of the content part when rendered.
- [var filename: String](mmspartcontent/filename.md)
  The file name of the MMS part.
- [var contentID: String](mmspartcontent/contentid.md)
  A unique identifier for the part.
- [var contentType: UTType?](mmspartcontent/contenttype.md)
  The content type of the part, as a Uniform Type Identifier.
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
### Working with custom headers
- [var customHeaders: [MMSPartContent.MMSCustomHeader]](mmspartcontent/customheaders.md)
  A dictionary of custom headers to send in the MMS message.
- [func addCustomHeader(MMSPartContent.MMSCustomHeader)](mmspartcontent/addcustomheader(_:).md)
  A helper function to add custom headers.
- [MMSPartContent.MMSCustomHeader](mmspartcontent/mmscustomheader.md)
  A structure that defines a custom header as a key-value pair.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var parts: [MMSPartContent]](mmscontent/parts.md)
  The individual parts of the MMS message.
- [var subject: String?](mmscontent/subject.md)
  The subject of the MMS message.
- [var headers: [String : String]](mmscontent/headers.md)
  Additional headers in a received MMS message, as a key-value dictionary of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent)*