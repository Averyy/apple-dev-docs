# CFXMLParserCopyDescriptionCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback function invoked by the parser when handling the information pointer.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias CFXMLParserCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

#### Return Value

A textual description of `info`. The caller is responsible for releasing this object.

## Parameters

- `info`: The program-defined context data you specified in the   structure when creating the parser.

## See Also

- [typealias CFXMLParserAddChildCallBack](cfxmlparseraddchildcallback.md)
  Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [typealias CFXMLParserCreateXMLStructureCallBack](cfxmlparsercreatexmlstructurecallback.md)
  Callback function invoked when the parser encounters an XML open tag.
- [typealias CFXMLParserEndXMLStructureCallBack](cfxmlparserendxmlstructurecallback.md)
  Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.
- [typealias CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md)
  Callback function invoked by the parser to notify your application that an error has occurred.
- [typealias CFXMLParserReleaseCallBack](cfxmlparserreleasecallback.md)
  Callback function invoked by the parser when it wants to release a reference to the information pointer.
- [typealias CFXMLParserResolveExternalEntityCallBack](cfxmlparserresolveexternalentitycallback.md)
  Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [typealias CFXMLParserRetainCallBack](cfxmlparserretaincallback.md)
  Callback function invoked by the parser when it needs another reference to the information pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparsercopydescriptioncallback)*