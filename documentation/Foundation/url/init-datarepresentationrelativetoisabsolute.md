# init(dataRepresentation:relativeTo:isAbsolute:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly created URL using the contents of the given data, relative to a base URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(dataRepresentation: Data, relativeTo base: URL?, isAbsolute: Bool = false)
```

#### Discussion

If the data representation isn’t a legal URL string as ASCII bytes, the URL object may not behave as expected. This initializer returns nil if it can’t form a valid URL from the provided string.

## See Also

- [var dataRepresentation: Data](url/datarepresentation.md)
  The data representation of the URL’s relativeString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(datarepresentation:relativeto:isabsolute:))*