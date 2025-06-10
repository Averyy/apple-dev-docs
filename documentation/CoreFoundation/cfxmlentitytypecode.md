# CFXMLEntityTypeCode

**Framework**: Core Foundation  
**Kind**: enum

The entity type identification codes that the parser uses to describe XML entities.

**Availability**:
- macOS ?+

## Declaration

```swift
enum CFXMLEntityTypeCode
```

#### Overview

These codes are used with the [`CFXMLEntityInfo`](cfxmlentityinfo.md) and [`CFXMLEntityReferenceInfo`](cfxmlentityreferenceinfo.md) structures.

## Topics

### Constants
- [CFXMLEntityTypeCode.parameter](cfxmlentitytypecode/parameter.md)
  Implies a parsed, internal entity.
- [CFXMLEntityTypeCode.parsedInternal](cfxmlentitytypecode/parsedinternal.md)
  Indicates a parsed, internal entity.
- [CFXMLEntityTypeCode.parsedExternal](cfxmlentitytypecode/parsedexternal.md)
  Indicates a parsed, external entity.
- [CFXMLEntityTypeCode.unparsed](cfxmlentitytypecode/unparsed.md)
  Indicates an unparsed entity.
- [CFXMLEntityTypeCode.character](cfxmlentitytypecode/character.md)
  Indicates a character entity type.
### Initializers
- [init?(rawValue: CFIndex)](cfxmlentitytypecode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Node Current Version](1443311-node-current-version.md)
  The version of a CFXMLNode object.
- [enum CFXMLNodeTypeCode](cfxmlnodetypecode.md)
  The various XML data type identification codes that the parser uses to describe XML structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlentitytypecode)*