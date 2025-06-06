# standardizedFileURL

**Framework**: Foundation  
**Kind**: property

A standardized version of the path of a file URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var standardizedFileURL: URL { get }
```

#### Discussion

If the `isFileURL` is false, this method returns `self`.

## See Also

- [var baseURL: URL?](url/baseurl.md)
  The base URL.
- [var absoluteString: String](url/absolutestring.md)
  The absolute string for the URL.
- [var absoluteURL: URL](url/absoluteurl.md)
  The absolute URL.
- [var relativePath: String](url/relativepath.md)
  The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.
- [var relativeString: String](url/relativestring.md)
  The relative portion of a URL.
- [var standardized: URL](url/standardized.md)
  A version of the URL with any instances of “..” or “.” resolved in its path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/standardizedfileurl)*