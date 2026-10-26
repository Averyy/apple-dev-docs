# XMLNode.Kind

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

`NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [`init(kind:)`](./init%28kind%29.md) and [`init(kind:options:)`](./init%28kind,options%29.md):

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum Kind
```

```c
enum NSXMLNodeKind : NSUInteger;
```

## Topics

### Constants
- [XMLNode.Kind.invalid](./kind-swift.enum/invalid.md)
  Indicates a node object created without a valid kind being specified (as returned by the [`kind`](./kind-swift.property.md) method).
- [XMLNode.Kind.document](./kind-swift.enum/document.md)
  Specifies a document node.
- [XMLNode.Kind.element](./kind-swift.enum/element.md)
  Specifies an element node.
- [XMLNode.Kind.attribute](./kind-swift.enum/attribute.md)
  Specifies an attribute node
- [XMLNode.Kind.namespace](./kind-swift.enum/namespace.md)
  Specifies a namespace node.
- [XMLNode.Kind.processingInstruction](./kind-swift.enum/processinginstruction.md)
  Specifies a processing-instruction node.
- [XMLNode.Kind.comment](./kind-swift.enum/comment.md)
  Specifies a comment node.
- [XMLNode.Kind.text](./kind-swift.enum/text.md)
  Specifies a text node.
- [XMLNode.Kind.DTDKind](./kind-swift.enum/dtdkind.md)
  Specifies a document-type declaration (DTD) node.
- [XMLNode.Kind.entityDeclaration](./kind-swift.enum/entitydeclaration.md)
  Specifies an entity-declaration node.
- [XMLNode.Kind.attributeDeclaration](./kind-swift.enum/attributedeclaration.md)
  Specifies an attribute-list declaration node.
- [XMLNode.Kind.elementDeclaration](./kind-swift.enum/elementdeclaration.md)
  Specifies an element declaration node.
- [XMLNode.Kind.notationDeclaration](./kind-swift.enum/notationdeclaration.md)
  Specifies a notation declaration node.
### Initializers
- [init?(rawValue: UInt)](./kind-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [XMLNode.Options](./options.md)
  These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [`XMLDocument`](../xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [`init(kind:options:)`](./init%28kind,options%29.md) and [`xmlString(options:)`](./xmlstring%28options%29.md).
- [NSXMLNodeOptionsNone](../nsxmlnodeoptions/nsxmlnodeoptionsnone.md)
  No options are requested for this input or output action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/kind-swift.enum)*