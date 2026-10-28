# absoluteURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The absolute URL.

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
var absoluteURL: URL { get }
```

## Discussion

If the URL is itself absolute, this returns `self`.

## See Also

### Accessing URL representations
- [var baseURL: URL?](./baseurl.md)
  The base URL.
- [var absoluteString: String](./absolutestring.md)
  The absolute string for the URL.
- [var relativePath: String](./relativepath.md)
  The relative path of the URL if the URL conforms to RFC 3986, otherwise nil.
- [var relativeString: String](./relativestring.md)
  The relative portion of a URL.
- [var standardized: URL](./standardized.md)
  A version of the URL with any instances of “..” or “.” resolved in its path.
- [var standardizedFileURL: URL](./standardizedfileurl.md)
  A standardized version of the path of a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/absoluteurl)*