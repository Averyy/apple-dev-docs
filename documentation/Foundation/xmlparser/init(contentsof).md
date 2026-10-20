# init(contentsOf:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a parser with the XML content referenced by the given URL.

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
convenience init?(contentsOf url: URL)
```

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) url;
```

#### Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

## Parameters

- `url`: An [`NSURL`](../nsurl.md) object specifying a URL. The URL must be fully qualified and refer to a scheme that is supported by the `NSURL` class.

## See Also

### Related Documentation
- [Event-Driven XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/XMLParsing.html#//apple_ref/doc/uid/10000186i)
### Initializing a Parser Object
- [init(data: Data)](./init%28data%29.md)
  Initializes a parser with the XML contents encapsulated in a given data object.
- [convenience init(stream: InputStream)](./init%28stream%29.md)
  Initializes a parser with the XML contents from the specified stream and parses it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/init(contentsof:))*