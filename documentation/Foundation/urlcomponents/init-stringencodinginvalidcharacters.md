# init(string:encodingInvalidCharacters:)

**Framework**: Foundation  
**Kind**: init

Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

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

- `string`: The URL string to parse.
- `encodingInvalidCharacters`: A Boolean value that indicates whether the initializer attempts to encode any invalid characters in  .

## See Also

- [init()](urlcomponents/init.md)
  Creates a URL components instance without defining any of the components.
- [init?(string: String)](urlcomponents/init(string:).md)
  Creates a URL components instance from a URL string.
- [init?(url: URL, resolvingAgainstBaseURL: Bool)](urlcomponents/init(url:resolvingagainstbaseurl:).md)
  Creates a URL components instance from a URL string, optionally resolving against a base URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/init(string:encodinginvalidcharacters:))*