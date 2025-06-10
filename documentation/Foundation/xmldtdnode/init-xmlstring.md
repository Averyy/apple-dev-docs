# init(xmlString:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSXMLDTDNode` object initialized with the DTD declaration in a given string.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(xmlString string: String)
```

#### Return Value

An `NSXMLDTDNode` object initialized with the DTD declaration in `string`. Returns `nil` if initialization did not succeed, as might occur if the passed-in declaration is malformed.

#### Discussion

The node kind (NSXMLNode) assigned to the returned object—element, attribute, entity, or notation declaration— is based on the full XML string that is parsed. To assign a subkind, set the [`dtdKind`](xmldtdnode/dtdkind-swift.property.md) property.

You may also use the [`dtdNode(withXMLString:)`](xmlnode/dtdnode(withxmlstring:).md) or [`init(kind:)`](xmlnode/init(kind:).md) methods to create `NSXMLDTDNode` instances. However, you cannot use the latter method to create `NSXMLDTDNode` instances for attribute-list declarations.

## Parameters

- `string`: The DTD declaration.

## See Also

- [Tree-Based XML Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/init(xmlstring:))*