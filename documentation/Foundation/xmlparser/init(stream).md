# init(stream:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithStream:(NSInputStream *) stream;
```

## Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

## Parameters

- `stream`: The input stream. The content is incrementally loaded from the specified stream and parsed. The `NSXMLParser` will open the stream, and synchronously read from it without scheduling it.

## See Also

### Initializing a Parser Object
- [convenience init?(contentsOf: URL)](./init%28contentsof%29.md)
  Initializes a parser with the XML content referenced by the given URL.
- [init(data: Data)](./init%28data%29.md)
  Initializes a parser with the XML contents encapsulated in a given data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/init(stream:))*