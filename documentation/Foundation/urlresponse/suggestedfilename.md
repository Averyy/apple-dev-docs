# suggestedFilename

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A suggested filename for the response data.

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
var suggestedFilename: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * suggestedFilename;
```

#### Discussion

Accessing this property attempts to generate a filename using the following information, in order:

1. A filename specified using the content disposition header.
2. The last path component of the URL.
3. The host of the URL.

If the host of URL can’t be converted to a valid filename, the filename “unknown” is used.

In most cases, this property appends the proper file extension based on the MIME type. Accessing this property always returns a valid filename regardless of whether the resource is saved to disk.

## See Also

### Getting the response properties
- [var expectedContentLength: Int64](./expectedcontentlength.md)
  The expected length of the response’s content.
- [var mimeType: String?](./mimetype.md)
  The MIME type of the response.
- [var textEncodingName: String?](./textencodingname.md)
  The name of the text encoding provided by the response’s originating source.
- [var url: URL?](./url.md)
  The URL for the response.
- [NSURLResponseUnknownLength](../nsurlresponseunknownlength.md)
  The response length cannot be determined in advance of receiving the data from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/suggestedfilename)*