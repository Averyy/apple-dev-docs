# init(name:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSXMLElement` object initialized with the specified name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(name: String)
```

```objc
- (instancetype) initWithName:(NSString *) name;
```

#### Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

#### Discussion

The XML string representation of this object is `<``name``></``name``>`. This method invokes [`init(name:uri:)`](./init%28name,uri%29-1r286.md) with the URI parameter set to `nil`.

## Parameters

- `name`: A string specifying the name of the element.

## See Also

### Related Documentation
- [Tree-Based XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)
### Initializing NSXMLElement Objects
- [convenience init(name: String, stringValue: String?)](./init%28name,stringvalue%29.md)
  Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [init(name: String, uri: String?)](./init%28name,uri%29-1r286.md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [init(xmlString: String) throws](./init%28xmlstring%29-7vkg7.md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](./init%28kind,options%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(name:))*