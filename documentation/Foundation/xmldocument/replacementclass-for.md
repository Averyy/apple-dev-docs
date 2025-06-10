# replacementClass(for:)

**Framework**: Foundation  
**Kind**: method

Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func replacementClass(for cls: AnyClass) -> AnyClass
```

#### Return Value

The substituted class.

#### Discussion

For example, if you have a custom subclass of [`XMLElement`](xmlelement.md) that you want to be used in place of `NSXMLElement`, you would make the following override:

```objc
+ (Class)replacementClassForClass:(Class)currentClass {
    if ( currentClass == [NSXMLElement class] ) {
        return [MyCustomElementClass class];
    }
}
```

This method is invoked before a document is parsed. The substituted class must be a subclass of [`XMLNode`](xmlnode.md), `NSXMLDocument`, `NSXMLElement`, [`XMLDTD`](xmldtd.md), or [`XMLDTDNode`](xmldtdnode.md).

## Parameters

- `cls`: A   object identifying an NSXML class that is to be replaced by your custom class.

## See Also

- [func setRootElement(XMLElement)](xmldocument/setrootelement(_:).md)
  Set the root element of the receiver.
- [convenience init(contentsOf: URL, options: XMLNode.Options) throws](xmldocument/init(contentsof:options:).md)
  Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [init(data: Data, options: XMLNode.Options) throws](xmldocument/init(data:options:).md)
  Initializes and returns an `NSXMLDocument` object created from an [`NSData`](nsdata.md) object.
- [init(rootElement: XMLElement?)](xmldocument/init(rootelement:).md)
  Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [convenience init(xmlString: String, options: XMLNode.Options) throws](xmldocument/init(xmlstring:options:).md)
  Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/replacementclass(for:))*