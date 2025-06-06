# textEncodingName

**Framework**: Foundation  
**Kind**: property

The text encoding to use.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let textEncodingName: NSAttributedString.DocumentReadingOptionKey
```

#### Discussion

[`NSString`](nsstring.md) containing the name, IANA or otherwise, of a text encoding to override any encoding specified in an HTML document. Mutually exclusive with [`characterEncoding`](nsattributedstring/documentreadingoptionkey/characterencoding.md). The previous string constant was `@"TextEncodingName"`.

## See Also

- [static let baseURL: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/baseurl.md)
  The base URL for HTML documents.
- [static let characterEncoding: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/characterencoding.md)
  The string encoding.
- [static let defaultAttributes: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/defaultattributes.md)
  The default attributes to apply to plain files.
- [static let documentType: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/documenttype.md)
  The document type.
- [static let fileType: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/filetype.md)
  The file type.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/readaccessurl.md)
  The local files WebKit can access when loading content.
- [static let textSizeMultiplier: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/textsizemultiplier.md)
  The scale factor for font sizes.
- [static let timeout: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/timeout.md)
  The time, in seconds, to wait for a document to finish loading.
- [static let webPreferences: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/webpreferences.md)
  A WebPreferences object.
- [static let webResourceLoadDelegate: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/webresourceloaddelegate.md)
  An object to serve as the web resource loading delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/textencodingname)*