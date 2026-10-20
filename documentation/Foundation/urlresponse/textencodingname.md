# textEncodingName

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSString * textEncodingName;
```

#### Discussion

If no text encoding was provided by the protocol, this property’s value is `nil`.

You can convert this string to a `CFStringEncoding` value by calling [`CFStringConvertIANACharSetNameToEncoding(_:)`](../../CoreFoundation/cfstringconvertianacharsetnametoencoding%28_%29.md). You can subsequently convert that value to an `NSStringEncoding` value by calling [`CFStringConvertEncodingToNSStringEncoding(_:)`](../../CoreFoundation/cfstringconvertencodingtonsstringencoding%28_%29.md).

## See Also

### Getting the response properties
- [var expectedContentLength: Int64](./expectedcontentlength.md)
  The expected length of the response’s content.
- [var suggestedFilename: String?](./suggestedfilename.md)
  A suggested filename for the response data.
- [var mimeType: String?](./mimetype.md)
  The MIME type of the response.
- [var url: URL?](./url.md)
  The URL for the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/textencodingname)*