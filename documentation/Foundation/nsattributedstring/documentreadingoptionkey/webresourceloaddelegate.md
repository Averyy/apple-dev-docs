# webResourceLoadDelegate

**Framework**: Foundation  
**Kind**: property

An object to serve as the web resource loading delegate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let webResourceLoadDelegate: NSAttributedString.DocumentReadingOptionKey
```

#### Discussion

For HTML only. The value is an [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class).

If not present, a default delegate is used that permits the loading of subsidiary resources but does not respond to authentication challenges. The previous string constant was `@"WebResourceLoadDelegate"`.

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
- [static let textEncodingName: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/textencodingname.md)
  The text encoding to use.
- [static let textSizeMultiplier: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/textsizemultiplier.md)
  The scale factor for font sizes.
- [static let timeout: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/timeout.md)
  The time, in seconds, to wait for a document to finish loading.
- [static let webPreferences: NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey/webpreferences.md)
  A WebPreferences object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/webresourceloaddelegate)*