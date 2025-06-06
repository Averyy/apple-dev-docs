# textEncodingName

**Framework**: Foundation  
**Kind**: property

The name of the text encoding provided by the response’s originating source.

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
var textEncodingName: String? { get }
```

#### Discussion

If no text encoding was provided by the protocol, this property’s value is `nil`.

You can convert this string to a `CFStringEncoding` value by calling [`CFStringConvertIANACharSetNameToEncoding(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFStringConvertIANACharSetNameToEncoding(_:)). You can subsequently convert that value to an `NSStringEncoding` value by calling [`CFStringConvertEncodingToNSStringEncoding(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFStringConvertEncodingToNSStringEncoding(_:)).

## See Also

- [var expectedContentLength: Int64](urlresponse/expectedcontentlength.md)
  The expected length of the response’s content.
- [var suggestedFilename: String?](urlresponse/suggestedfilename.md)
  A suggested filename for the response data.
- [var mimeType: String?](urlresponse/mimetype.md)
  The MIME type of the response.
- [var url: URL?](urlresponse/url.md)
  The URL for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/textencodingname)*