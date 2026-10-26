# expectedContentLength

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) long long expectedContentLength;
```

#### Discussion

This property’s value is [`NSURLResponseUnknownLength`](../nsurlresponseunknownlength.md) if the length can’t be determined.

Some protocol implementations report the content length as part of the response, but not all protocols guarantee to deliver that amount of data. Your app should be prepared to deal with more or less data.

## See Also

### Getting the response properties
- [var suggestedFilename: String?](./suggestedfilename.md)
  A suggested filename for the response data.
- [var mimeType: String?](./mimetype.md)
  The MIME type of the response.
- [var textEncodingName: String?](./textencodingname.md)
  The name of the text encoding provided by the response’s originating source.
- [var url: URL?](./url.md)
  The URL for the response.
- [NSURLResponseUnknownLength](../nsurlresponseunknownlength.md)
  The response length cannot be determined in advance of receiving the data from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/expectedcontentlength)*