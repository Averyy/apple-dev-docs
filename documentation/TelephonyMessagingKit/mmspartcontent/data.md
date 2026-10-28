# data

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The raw data used for the MMS content part.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var data: Data
```

## Discussion

Interpreting this value depends on the part’s [`contentType`](./contenttype.md). For example, the data for a file attachment can be the file’s contents in binary. For file attachments, this can be the file contents in binary.

> 💡 **Tip**: When sending an MMS message that includes text, convert the text string to a [`Data`](../../Foundation/data.md) instance; for example, `let textData = myString.data(using: .utf8)`.

## See Also

### Accessing part properties
- [var disposition: MMSPartContent.MMSDispositionType](./disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [MMSPartContent.MMSDispositionType](./mmsdispositiontype.md)
  A structure that defines the disposition of the content part when rendered.
- [var filename: String](./filename.md)
  The file name of the MMS part.
- [var contentID: String](./contentid.md)
  A unique identifier for the part.
- [var contentType: UTType?](./contenttype.md)
  The content type of the part, as a Uniform Type Identifier.
- [struct UTType](../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/data)*