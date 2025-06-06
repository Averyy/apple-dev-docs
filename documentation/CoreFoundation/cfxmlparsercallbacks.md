# CFXMLParserCallBacks

**Framework**: Core Foundation  
**Kind**: struct

Contains version information and function pointers to callbacks needed when parsing XML.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLParserCallBacks
```

#### Overview

This structure is passed to one of the `CFXMLParserCreate...` functions. Only the `createXMLStructure`, `addChild`, and `endXMLStructure` fields are required. Set the others to `NULL` if you don’t wish to implement them.

## Topics

### Initializers
- [init()](cfxmlparsercallbacks/init.md)
- [init(version: CFIndex, createXMLStructure: CFXMLParserCreateXMLStructureCallBack!, addChild: CFXMLParserAddChildCallBack!, endXMLStructure: CFXMLParserEndXMLStructureCallBack!, resolveExternalEntity: CFXMLParserResolveExternalEntityCallBack!, handleError: CFXMLParserHandleErrorCallBack!)](cfxmlparsercallbacks/init(version:createxmlstructure:addchild:endxmlstructure:resolveexternalentity:handleerror:).md)
### Instance Properties
- [var addChild: CFXMLParserAddChildCallBack!](cfxmlparsercallbacks/addchild.md)
  Called when a child is added.
- [var createXMLStructure: CFXMLParserCreateXMLStructureCallBack!](cfxmlparsercallbacks/createxmlstructure.md)
  Called when an XML structure is created.
- [var endXMLStructure: CFXMLParserEndXMLStructureCallBack!](cfxmlparsercallbacks/endxmlstructure.md)
  Called when an XML structure has ended.
- [var handleError: CFXMLParserHandleErrorCallBack!](cfxmlparsercallbacks/handleerror.md)
  Called when a parse error needs to be handled.
- [var resolveExternalEntity: CFXMLParserResolveExternalEntityCallBack!](cfxmlparsercallbacks/resolveexternalentity.md)
  Called when an external entity needs to be resolved.
- [var version: CFIndex](cfxmlparsercallbacks/version.md)
  Version number. Must be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CFXMLParserContext](cfxmlparsercontext.md)
  Contains version information and function pointers to callbacks used when handling a program-defined context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparsercallbacks)*