# componentsWithString:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a URL components object by parsing a URL in string form.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) componentsWithString:(NSString *) URLString;
```

## Return Value

Returns the new URL components object, or `nil` if the URL string could not be parsed.

## Parameters

- `URLString`: The URL string to parse.

## See Also

### Creating URL components
- [+ componentsWithString:encodingInvalidCharacters:](./componentswithstring_encodinginvalidcharacters_.md)
  Returns a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/componentswithstring:)*