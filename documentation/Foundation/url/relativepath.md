# relativePath

**Framework**: Foundation  
**Kind**: property

The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.

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
var relativePath: String { get }
```

#### Return Value

The relative path, or an empty string if the URL has an empty path.

#### Discussion

> **Note**:  This function resolve against the base `URL`.

## See Also

- [var baseURL: URL?](url/baseurl.md)
  The base URL.
- [var absoluteString: String](url/absolutestring.md)
  The absolute string for the URL.
- [var absoluteURL: URL](url/absoluteurl.md)
  The absolute URL.
- [var relativeString: String](url/relativestring.md)
  The relative portion of a URL.
- [var standardized: URL](url/standardized.md)
  A version of the URL with any instances of “..” or “.” resolved in its path.
- [var standardizedFileURL: URL](url/standardizedfileurl.md)
  A standardized version of the path of a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/relativepath)*