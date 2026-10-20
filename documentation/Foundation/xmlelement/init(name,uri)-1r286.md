# init(name:uri:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSXMLElement` object initialized with the specified name and URI.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(name: String, uri URI: String?)
```

```objc
- (instancetype) initWithName:(NSString *) name URI:(NSString *) URI;
```

#### Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

#### Discussion

You can look up the namespace prefix for this element node based on its URI using [`resolvePrefix(forNamespaceURI:)`](./resolveprefix%28fornamespaceuri%29.md).  This method is the primary initializer for the `NSXMLElement` class.

## Parameters

- `name`: A string that specifies the qualified name of the element.
- `URI`: A string that specifies the namespace URI associated with the element.

## See Also

### Initializing NSXMLElement Objects
- [convenience init(name: String)](./init%28name%29.md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [convenience init(name: String, stringValue: String?)](./init%28name,stringvalue%29.md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(xmlString: String) throws](./init%28xmlstring%29-7vkg7.md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](./init%28kind,options%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(name:uri:)-1r286)*