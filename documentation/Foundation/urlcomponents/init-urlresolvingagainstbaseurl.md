# init(url:resolvingAgainstBaseURL:)

**Framework**: Foundation  
**Kind**: init

Creates a URL components instance from a URL string, optionally resolving against a base URL.

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
init?(url: URL, resolvingAgainstBaseURL resolve: Bool)
```

## Parameters

- `url`: The URL string to parse.
- `resolve`: Controls whether the initializer resolves the URL against its base URL before parsing. If   is a relative URL, setting   to   creates components using the   property.

## See Also

- [init()](urlcomponents/init.md)
  Creates a URL components instance without defining any of the components.
- [init?(string: String)](urlcomponents/init(string:).md)
  Creates a URL components instance from a URL string.
- [init?(string: String, encodingInvalidCharacters: Bool)](urlcomponents/init(string:encodinginvalidcharacters:).md)
  Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/init(url:resolvingagainstbaseurl:))*