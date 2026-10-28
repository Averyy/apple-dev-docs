# init(name:stringValue:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(name: String, stringValue string: String?)
```

```objc
- (instancetype) initWithName:(NSString *) name stringValue:(NSString *) string;
```

## Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

## Discussion

The string representation of this object is `<``name``>``string``</``name``>`.

## Parameters

- `name`: A string specifying the name of the element.
- `string`: The string value of the receiver’s text node.

## See Also

### Initializing NSXMLElement Objects
- [convenience init(name: String)](./init%28name%29.md)
  Returns an `NSXMLElement` object initialized with the specified name.
- [init(name: String, uri: String?)](./init%28name,uri%29-1r286.md)
  Returns an `NSXMLElement` object initialized with the specified name and URI.
- [init(xmlString: String) throws](./init%28xmlstring%29-7vkg7.md)
  Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [convenience init(kind: XMLNode.Kind, options: XMLNode.Options)](./init%28kind,options%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlelement/init(name:stringvalue:))*