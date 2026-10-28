# componentsWithString:encodingInvalidCharacters:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
+ (instancetype) componentsWithString:(NSString *) URLString encodingInvalidCharacters:(BOOL) encodingInvalidCharacters;
```

## Return Value

A URL components instance from the provided string, optionally with invalid characters percent-encoded.

## Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the method returns `nil`.

## Parameters

- `URLString`: The URL string to parse.
- `encodingInvalidCharacters`: A Boolean value that indicates whether the initializer attempts to encode any invalid characters in `URLString`.

## See Also

### Creating URL components
- [+ componentsWithString:](./componentswithstring_.md)
  Returns a URL components object by parsing a URL in string form.
- [+ componentsWithURL:resolvingAgainstBaseURL:](./componentswithurl_resolvingagainstbaseurl_.md)
  Returns a URL components object by parsing the URL from an `NSURL` object.
- [init()](./init%28%29.md)
  Creates a URL components object with all components left undefined.
- [init?(string: String)](./init%28string%29.md)
  Creates a URL components object by parsing a URL in string form.
- [init?(string: String, encodingInvalidCharacters: Bool)](./init%28string,encodinginvalidcharacters%29.md)
  Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(url: URL, resolvingAgainstBaseURL: Bool)](./init%28url,resolvingagainstbaseurl%29-3bbte.md)
  Creates a URL components object by parsing the URL from an `NSURL` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/componentswithstring:encodinginvalidcharacters:)*