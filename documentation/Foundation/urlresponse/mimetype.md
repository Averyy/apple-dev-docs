# mimeType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSString * MIMEType;
```

## Discussion

The MIME type is often provided by the response’s originating source. However, that value may be changed or corrected by a protocol implementation if it can be determined that the response’s source reported the information incorrectly.

If the response’s originating source does not provide a MIME type, an attempt to guess the MIME type may be made.

## See Also

### Getting the response properties
- [var expectedContentLength: Int64](./expectedcontentlength.md)
  The expected length of the response’s content.
- [var suggestedFilename: String?](./suggestedfilename.md)
  A suggested filename for the response data.
- [var textEncodingName: String?](./textencodingname.md)
  The name of the text encoding provided by the response’s originating source.
- [var url: URL?](./url.md)
  The URL for the response.
- [NSURLResponseUnknownLength](../nsurlresponseunknownlength.md)
  The response length cannot be determined in advance of receiving the data from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/mimetype)*