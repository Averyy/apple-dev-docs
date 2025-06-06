# CFXMLParserAddChildCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias CFXMLParserAddChildCallBack = (CFXMLParser?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

If the [`CFXMLParserCreateXMLStructureCallBack`](cfxmlparsercreatexmlstructurecallback.md) function returns NULL for a given structure, that structure is omitted entirely, and this callback will  be called for either a NULL child or parent.

## Parameters

- `parser`: The CFXMLParser object making the callback.
- `parent`: The program-defined value representing the XML element to whom   is being added. This value was returned by the   callback when this element’s open tag was detected.
- `child`: The program-defined value representing the XML element that is being added to  . This value was returned by the   callback when this element’s open tag was detected.
- `info`: The program-defined context data you specified in the   structure when creating the parser.

## See Also

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
- [typealias CFXMLParserResolveExternalEntityCallBack](cfxmlparserresolveexternalentitycallback.md)
  Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [typealias CFXMLParserRetainCallBack](cfxmlparserretaincallback.md)
  Callback function invoked by the parser when it needs another reference to the information pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparseraddchildcallback)*