# init(stream:)

**Framework**: Foundation  
**Kind**: init

Initializes a parser with the XML contents from the specified stream and parses it.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(stream: InputStream)
```

#### Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

## Parameters

- `stream`: The input stream. The content is incrementally loaded from the specified stream and parsed. The   will open the stream, and synchronously read from it without scheduling it.

## See Also

- [convenience init?(contentsOf: URL)](xmlparser/init(contentsof:).md)
  Initializes a parser with the XML content referenced by the given URL.
- [init(data: Data)](xmlparser/init(data:).md)
  Initializes a parser with the XML contents encapsulated in a given data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/init(stream:))*