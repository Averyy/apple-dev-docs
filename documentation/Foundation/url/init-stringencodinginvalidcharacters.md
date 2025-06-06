# init(string:encodingInvalidCharacters:)

**Framework**: Foundation  
**Kind**: init

Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init?(string: String, encodingInvalidCharacters: Bool)
```

#### Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the initializer returns `nil`.

## Parameters

- `string`: A URL location.
- `encodingInvalidCharacters`: A Boolean value that indicates whether the initializer attempts to encode any invalid characters in  .

## See Also

- [init?(string: String)](url/init(string:).md)
  Creates a URL instance from the provided string.
- [init?(string: String, relativeTo: URL?)](url/init(string:relativeto:).md)
  Creates a URL instance from the provided string, relative to another URL.
- [init(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-3ic6f.md)
  Creates a URL that refers to a location specified by resolving bookmark data.
- [init?(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-97e6x.md)
  Initializes a URL that refers to a location specified by resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(string:encodinginvalidcharacters:))*