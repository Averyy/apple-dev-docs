# init(data:)

**Framework**: Foundation  
**Kind**: init

Initializes a parser with the XML contents encapsulated in a given data object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(data: Data)
```

#### Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

#### Discussion

This method is the designated initializer.

## Parameters

- `data`: An   object containing XML markup.

## See Also

- [convenience init?(contentsOf: URL)](xmlparser/init(contentsof:).md)
  Initializes a parser with the XML content referenced by the given URL.
- [convenience init(stream: InputStream)](xmlparser/init(stream:).md)
  Initializes a parser with the XML contents from the specified stream and parses it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/init(data:))*