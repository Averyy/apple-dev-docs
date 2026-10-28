# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a URL components object with all components left undefined.

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
init()
```

```objc
- (instancetype) init;
```

## Return Value

Returns the initialized URL components object, or `nil` if an error occurs.

## See Also

### Creating URL components
- [init?(string: String)](./init%28string%29.md)
  Creates a URL components object by parsing a URL in string form.
- [init?(string: String, encodingInvalidCharacters: Bool)](./init%28string,encodinginvalidcharacters%29.md)
  Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(url: URL, resolvingAgainstBaseURL: Bool)](./init%28url,resolvingagainstbaseurl%29-3bbte.md)
  Creates a URL components object by parsing the URL from an `NSURL` object.
- [+ componentsWithString:](./componentswithstring_.md)
  Returns a URL components object by parsing a URL in string form.
- [+ componentsWithString:encodingInvalidCharacters:](./componentswithstring_encodinginvalidcharacters_.md)
  Returns a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [+ componentsWithURL:resolvingAgainstBaseURL:](./componentswithurl_resolvingagainstbaseurl_.md)
  Returns a URL components object by parsing the URL from an `NSURL` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/init())*