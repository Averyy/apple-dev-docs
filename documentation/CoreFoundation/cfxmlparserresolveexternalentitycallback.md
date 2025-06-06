# CFXMLParserResolveExternalEntityCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback function invoked by the parser to notify your application that an external entity has been referenced.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias CFXMLParserResolveExternalEntityCallBack = (CFXMLParser?, UnsafeMutablePointer<CFXMLExternalID>?, UnsafeMutableRawPointer?) -> Unmanaged<CFData>?
```

#### Return Value

The external entity or `NULL` if it should not be resolved.

#### Discussion

If this callback is not defined, the parser uses its internal routines to try and resolve the entity. Otherwise, if this callback returns NULL, a place holder for the external entity is inserted into the tree. In this manner, the parser’s client can prevent any external network or file accesses. This callback is optional.

## Parameters

- `parser`: The CFXMLParser object making the callback.
- `extID`: The identifier for the external entity.
- `info`: The program-defined context data you specified in the   structure when creating the parser.

## See Also

- [typealias CFXMLParserAddChildCallBack](cfxmlparseraddchildcallback.md)
  Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [typealias CFXMLParserCopyDescriptionCallBack](cfxmlparsercopydescriptioncallback.md)
  Callback function invoked by the parser when handling the information pointer.
- [typealias CFXMLParserCreateXMLStructureCallBack](cfxmlparsercreatexmlstructurecallback.md)
  Callback function invoked when the parser encounters an XML open tag.
- [typealias CFXMLParserEndXMLStructureCallBack](cfxmlparserendxmlstructurecallback.md)
  Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.
- [typealias CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md)
  Callback function invoked by the parser to notify your application that an error has occurred.
- [typealias CFXMLParserReleaseCallBack](cfxmlparserreleasecallback.md)
  Callback function invoked by the parser when it wants to release a reference to the information pointer.
- [typealias CFXMLParserRetainCallBack](cfxmlparserretaincallback.md)
  Callback function invoked by the parser when it needs another reference to the information pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparserresolveexternalentitycallback)*