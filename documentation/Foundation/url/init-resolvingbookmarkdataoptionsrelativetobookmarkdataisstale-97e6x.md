# init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)

**Framework**: Foundation  
**Kind**: init

Initializes a URL that refers to a location specified by resolving bookmark data.

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
init?(resolvingBookmarkData data: Data, options: URL.BookmarkResolutionOptions = [], relativeTo url: URL? = nil, bookmarkDataIsStale: inout Bool) throws
```

## See Also

- [init?(string: String)](url/init(string:).md)
  Creates a URL instance from the provided string.
- [init?(string: String, encodingInvalidCharacters: Bool)](url/init(string:encodinginvalidcharacters:).md)
  Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(string: String, relativeTo: URL?)](url/init(string:relativeto:).md)
  Creates a URL instance from the provided string, relative to another URL.
- [init(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-3ic6f.md)
  Creates a URL that refers to a location specified by resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-97e6x)*