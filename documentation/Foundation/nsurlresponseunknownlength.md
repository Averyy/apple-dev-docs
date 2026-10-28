# NSURLResponseUnknownLength

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

The response length cannot be determined in advance of receiving the data from the server.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
#define NSURLResponseUnknownLength
```

## Discussion

For example, [`NSURLResponseUnknownLength`](./nsurlresponseunknownlength.md) is returned when the server HTTP response does not include a `Content-Length` header.

## See Also

### Getting the response properties
- [var expectedContentLength: Int64](./urlresponse/expectedcontentlength.md)
  The expected length of the response’s content.
- [var suggestedFilename: String?](./urlresponse/suggestedfilename.md)
  A suggested filename for the response data.
- [var mimeType: String?](./urlresponse/mimetype.md)
  The MIME type of the response.
- [var textEncodingName: String?](./urlresponse/textencodingname.md)
  The name of the text encoding provided by the response’s originating source.
- [var url: URL?](./urlresponse/url.md)
  The URL for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlresponseunknownlength)*