# XMLNode.Kind

**Framework**: Foundation  
**Kind**: enum

`NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [`init(kind:)`](xmlnode/init(kind:).md) and [`init(kind:options:)`](xmlnode/init(kind:options:).md):

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum Kind
```

## Topics

### Constants
- [XMLNode.Kind.invalid](xmlnode/kind-swift.enum/invalid.md)
  Indicates a node object created without a valid kind being specified (as returned by the [`kind`](xmlnode/kind-swift.property.md) method).
- [XMLNode.Kind.document](xmlnode/kind-swift.enum/document.md)
  Specifies a document node.
- [XMLNode.Kind.element](xmlnode/kind-swift.enum/element.md)
  Specifies an element node.
- [XMLNode.Kind.attribute](xmlnode/kind-swift.enum/attribute.md)
  Specifies an attribute node
- [XMLNode.Kind.namespace](xmlnode/kind-swift.enum/namespace.md)
  Specifies a namespace node.
- [XMLNode.Kind.processingInstruction](xmlnode/kind-swift.enum/processinginstruction.md)
  Specifies a processing-instruction node.
- [XMLNode.Kind.comment](xmlnode/kind-swift.enum/comment.md)
  Specifies a comment node.
- [XMLNode.Kind.text](xmlnode/kind-swift.enum/text.md)
  Specifies a text node.
- [XMLNode.Kind.DTDKind](xmlnode/kind-swift.enum/dtdkind.md)
  Specifies a document-type declaration (DTD) node.
- [XMLNode.Kind.entityDeclaration](xmlnode/kind-swift.enum/entitydeclaration.md)
  Specifies an entity-declaration node.
- [XMLNode.Kind.attributeDeclaration](xmlnode/kind-swift.enum/attributedeclaration.md)
  Specifies an attribute-list declaration node.
- [XMLNode.Kind.elementDeclaration](xmlnode/kind-swift.enum/elementdeclaration.md)
  Specifies an element declaration node.
- [XMLNode.Kind.notationDeclaration](xmlnode/kind-swift.enum/notationdeclaration.md)
  Specifies a notation declaration node.
### Initializers
- [init?(rawValue: UInt)](xmlnode/kind-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [XMLNode.Options](xmlnode/options.md)
  These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [`XMLDocument`](xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [`init(kind:options:)`](xmlnode/init(kind:options:).md) and [`xmlString(options:)`](xmlnode/xmlstring(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/kind-swift.enum)*