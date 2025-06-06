# expectedContentLength

**Framework**: Foundation  
**Kind**: property

The expected length of the response’s content.

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
var expectedContentLength: Int64 { get }
```

#### Discussion

This property’s value is [`NSURLResponseUnknownLength`](nsurlresponseunknownlength.md) if the length can’t be determined.

Some protocol implementations report the content length as part of the response, but not all protocols guarantee to deliver that amount of data. Your app should be prepared to deal with more or less data.

## See Also

- [var suggestedFilename: String?](urlresponse/suggestedfilename.md)
  A suggested filename for the response data.
- [var mimeType: String?](urlresponse/mimetype.md)
  The MIME type of the response.
- [var textEncodingName: String?](urlresponse/textencodingname.md)
  The name of the text encoding provided by the response’s originating source.
- [var url: URL?](urlresponse/url.md)
  The URL for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/expectedcontentlength)*