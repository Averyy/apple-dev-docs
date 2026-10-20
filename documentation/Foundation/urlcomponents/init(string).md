# init(string:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a URL components instance from a URL string.

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

If `string` represents a malformed URL, this initializer returns `nil`.

## Parameters

- `string`: A URL location.

## See Also

### Creating URL components
- [init()](./init%28%29.md)
  Creates a URL components instance without defining any of the components.
- [init?(string: String, encodingInvalidCharacters: Bool)](./init%28string,encodinginvalidcharacters%29.md)
  Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(url: URL, resolvingAgainstBaseURL: Bool)](./init%28url,resolvingagainstbaseurl%29.md)
  Creates a URL components instance from a URL string, optionally resolving against a base URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/init(string:))*