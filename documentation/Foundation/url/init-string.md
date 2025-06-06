# init(string:)

**Framework**: Foundation  
**Kind**: init

Creates a URL instance from the provided string.

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
init?(string: String)
```

#### Discussion

> ❗ **Important**:  For apps linked on or after iOS 17 and aligned OS versions, [`URL`](url.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [`RFC 3986`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc3986.txt) parsing as [`URLComponents`](urlcomponents.md). This unifies the parsing behaviors of the `URL` and `URLComponents` APIs. Now, `URL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.

 For apps linked on or after iOS 17 and aligned OS versions, [`URL`](url.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [`RFC 3986`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc3986.txt) parsing as [`URLComponents`](urlcomponents.md). This unifies the parsing behaviors of the `URL` and `URLComponents` APIs. Now, `URL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.

This initializer returns `nil` if the string doesn’t represent a valid URL even after encoding invalid characters. To check if a URL string is strictly valid according to the RFC, use the new [`init(string:encodingInvalidCharacters:)`](url/init(string:encodinginvalidcharacters:).md) initializer and pass `encodingInvalidCharacters: false`. This leaves all characters as they are and returns `nil` if the URL string is explicitly invalid.

## Parameters

- `string`: A URL location.

## See Also

- [init?(string: String, encodingInvalidCharacters: Bool)](url/init(string:encodinginvalidcharacters:).md)
  Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(string: String, relativeTo: URL?)](url/init(string:relativeto:).md)
  Creates a URL instance from the provided string, relative to another URL.
- [init(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-3ic6f.md)
  Creates a URL that refers to a location specified by resolving bookmark data.
- [init?(resolvingBookmarkData: Data, options: URL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: inout Bool) throws](url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-97e6x.md)
  Initializes a URL that refers to a location specified by resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(string:))*