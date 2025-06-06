# init(url:resolvingAgainstBaseURL:)

**Framework**: Foundation  
**Kind**: init

Creates a URL components object by parsing the URL from an `NSURL` object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(url: URL, resolvingAgainstBaseURL resolve: Bool)
```

#### Return Value

Returns the initialized URL components object, or `nil` if the URL could not be parsed.

## Parameters

- `url`: The URL to parse.
- `resolve`: Controls whether the URL should be resolved against its base URL before parsing. If  , and if the   parameter contains a relative URL, the original URL is resolved against its base URL before parsing by calling the   method. Otherwise, the string portion is used by itself.

## See Also

- [init()](nsurlcomponents/init.md)
  Creates a URL components object with all components left undefined.
- [init?(string: String)](nsurlcomponents/init(string:).md)
  Creates a URL components object by parsing a URL in string form.
- [init?(string: String, encodingInvalidCharacters: Bool)](nsurlcomponents/init(string:encodinginvalidcharacters:).md)
  Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/init(url:resolvingagainstbaseurl:))*