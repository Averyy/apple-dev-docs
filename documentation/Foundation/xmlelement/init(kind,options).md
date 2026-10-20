# init(kind:options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(kind: XMLNode.Kind, options: XMLNode.Options = [])
```

```objc
- (instancetype) initWithKind:(NSXMLNodeKind) kind options:(NSXMLNodeOptions) options;
```

## See Also

### Initializing NSXMLElement Objects
- [convenience init(name: String)](./init%28name%29.md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [convenience init(name: String, stringValue: String?)](./init%28name,stringvalue%29.md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(name: String, uri: String?)](./init%28name,uri%29-1r286.md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [init(xmlString: String) throws](./init%28xmlstring%29-7vkg7.md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(kind:options:))*