# init(rootElement:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSXMLDocument` object initialized with a single child, the root element.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(rootElement element: XMLElement?)
```

```objc
- (instancetype) initWithRootElement:(NSXMLElement *) element;
```

## Return Value

An initialized `NSXMLDocument` object, or  `nil` if initialization fails for any reason.

## Parameters

- `element`: An [`XMLElement`](../xmlelement.md) object representing an XML element.

## See Also

### Initializing NSXMLDocument Objects
- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](./init%28contentsof,options%29.md)
  Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [init(data: Data, options: XMLNode.Options) throws](./init%28data,options%29.md)
  Initializes and returns an `NSXMLDocument` object created from an [`NSData`](../nsdata.md) object.
- [convenience init(xmlString: String, options: XMLNode.Options) throws](./init%28xmlstring,options%29-65m2r.md)
  Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.
- [class func replacementClass(for: AnyClass) -> AnyClass](./replacementclass%28for%29.md)
  Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/init(rootelement:))*