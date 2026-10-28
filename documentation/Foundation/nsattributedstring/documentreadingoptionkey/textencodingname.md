# textEncodingName

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The text encoding to use.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let textEncodingName: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

[`NSString`](../../nsstring.md) containing the name, IANA or otherwise, of a text encoding to override any encoding specified in an HTML document. Mutually exclusive with [`characterEncoding`](./characterencoding.md). The previous string constant was `@"TextEncodingName"`.

## See Also

### Getting the document options
- [static let baseURL: NSAttributedString.DocumentReadingOptionKey](./baseurl.md)
  The base URL for HTML documents.
- [static let characterEncoding: NSAttributedString.DocumentReadingOptionKey](./characterencoding.md)
  The string encoding.
- [static let defaultAttributes: NSAttributedString.DocumentReadingOptionKey](./defaultattributes.md)
  The default attributes to apply to plain files.
- [static let documentType: NSAttributedString.DocumentReadingOptionKey](./documenttype.md)
  The document type.
- [static let fileType: NSAttributedString.DocumentReadingOptionKey](./filetype.md)
  The file type.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](./readaccessurl.md)
  The local files WebKit can access when loading content.
- [static let textSizeMultiplier: NSAttributedString.DocumentReadingOptionKey](./textsizemultiplier.md)
  The scale factor for font sizes.
- [static let timeout: NSAttributedString.DocumentReadingOptionKey](./timeout.md)
  The time, in seconds, to wait for a document to finish loading.
- [static let webPreferences: NSAttributedString.DocumentReadingOptionKey](./webpreferences.md)
  A WebPreferences object.
- [static let webResourceLoadDelegate: NSAttributedString.DocumentReadingOptionKey](./webresourceloaddelegate.md)
  An object to serve as the web resource loading delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/textencodingname)*