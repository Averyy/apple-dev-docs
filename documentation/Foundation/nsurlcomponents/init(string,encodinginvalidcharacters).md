# init(string:encodingInvalidCharacters:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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
init?(string URLString: String, encodingInvalidCharacters: Bool)
```

```objc
- (instancetype) initWithString:(NSString *) URLString encodingInvalidCharacters:(BOOL) encodingInvalidCharacters;
```

#### Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the initializer returns `nil`.

## Parameters

- `URLString`: The URL string to parse.
- `encodingInvalidCharacters`: A Boolean value that indicates whether the initializer attempts to encode any invalid characters in `URLString`.

## See Also

### Creating URL components
- [init()](./init%28%29.md)
  Creates a URL components object with all components left undefined.
- [init?(string: String)](./init%28string%29.md)
  Creates a URL components object by parsing a URL in string form.
- [init?(url: URL, resolvingAgainstBaseURL: Bool)](./init%28url,resolvingagainstbaseurl%29-3bbte.md)
  Creates a URL components object by parsing the URL from an `NSURL` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/init(string:encodinginvalidcharacters:))*