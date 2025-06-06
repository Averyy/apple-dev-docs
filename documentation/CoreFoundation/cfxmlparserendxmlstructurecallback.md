# CFXMLParserEndXMLStructureCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias CFXMLParserEndXMLStructureCallBack = (CFXMLParser?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

As elements are encountered, this callback is called first, then the [`CFXMLParserAddChildCallBack`](cfxmlparseraddchildcallback.md) callback to add the new structure to its parent, then the [`CFXMLParserAddChildCallBack`](cfxmlparseraddchildcallback.md) callback (potentially several times) to add the new structure’s children to it, and then finally the [`CFXMLParserEndXMLStructureCallBack`](cfxmlparserendxmlstructurecallback.md) callback to show that the structure has been fully parsed.This callback is optional.

## Parameters

- `parser`: The CFXMLParser object making the callback.
- `xmlType`: The program-defined value representing the XML element whose end tag has been detected. This value was returned by the   callback.
- `info`: The program-defined context data you specified in the   structure when creating the parser.

## See Also

- [typealias CFXMLParserAddChildCallBack](cfxmlparseraddchildcallback.md)
  Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [typealias CFXMLParserCopyDescriptionCallBack](cfxmlparsercopydescriptioncallback.md)
  Callback function invoked by the parser when handling the information pointer.
- [typealias CFXMLParserCreateXMLStructureCallBack](cfxmlparsercreatexmlstructurecallback.md)
  Callback function invoked when the parser encounters an XML open tag.
- [typealias CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md)
  Callback function invoked by the parser to notify your application that an error has occurred.
- [typealias CFXMLParserReleaseCallBack](cfxmlparserreleasecallback.md)
  Callback function invoked by the parser when it wants to release a reference to the information pointer.
- [typealias CFXMLParserResolveExternalEntityCallBack](cfxmlparserresolveexternalentitycallback.md)
  Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [typealias CFXMLParserRetainCallBack](cfxmlparserretaincallback.md)
  Callback function invoked by the parser when it needs another reference to the information pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparserendxmlstructurecallback)*