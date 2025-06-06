# mimeType

**Framework**: Foundation  
**Kind**: property

The MIME type of the response.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var mimeType: String? { get }
```

#### Discussion

The MIME type is often provided by the response’s originating source. However, that value may be changed or corrected by a protocol implementation if it can be determined that the response’s source reported the information incorrectly.

If the response’s originating source does not provide a MIME type, an attempt to guess the MIME type may be made.

## See Also

- [var expectedContentLength: Int64](urlresponse/expectedcontentlength.md)
  The expected length of the response’s content.
- [var suggestedFilename: String?](urlresponse/suggestedfilename.md)
  A suggested filename for the response data.
- [var textEncodingName: String?](urlresponse/textencodingname.md)
  The name of the text encoding provided by the response’s originating source.
- [var url: URL?](urlresponse/url.md)
  The URL for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/mimetype)*