# init(data:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithData:(NSData *) data;
```

## Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

## Discussion

This method is the designated initializer.

## Parameters

- `data`: An [`NSData`](../nsdata.md) object containing XML markup.

## See Also

### Initializing a Parser Object
- [convenience init?(contentsOf: URL)](./init%28contentsof%29.md)
  Initializes a parser with the XML content referenced by the given URL.
- [convenience init(stream: InputStream)](./init%28stream%29.md)
  Initializes a parser with the XML contents from the specified stream and parses it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/init(data:))*