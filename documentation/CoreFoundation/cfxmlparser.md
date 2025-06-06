# CFXMLParser

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- macOS ?+

## Declaration

```swift
class CFXMLParser
```

#### Overview

CFXMLParser provides an XML parser you can use to find and extract data in XML documents. You can use a high-level interface to load an XML document into a Core Foundation collection object. A low-level callback-based interface allows you to perform any action you wish on an XML structured type when it is detected by the parser. This opaque type is relevant for applications that need information about an XML document’s structure or content.

## Topics

### Callbacks
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
- [typealias CFXMLParserResolveExternalEntityCallBack](cfxmlparserresolveexternalentitycallback.md)
  Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [typealias CFXMLParserRetainCallBack](cfxmlparserretaincallback.md)
  Callback function invoked by the parser when it needs another reference to the information pointer.
### Data Types
- [struct CFXMLParserCallBacks](cfxmlparsercallbacks.md)
  Contains version information and function pointers to callbacks needed when parsing XML.
- [struct CFXMLParserContext](cfxmlparsercontext.md)
  Contains version information and function pointers to callbacks used when handling a program-defined context.
### Constants
- [struct CFXMLParserStatusCode](cfxmlparserstatuscode.md)
  The various status and error flags that can be returned by the parser.
- [struct CFXMLParserOptions](cfxmlparseroptions.md)
  Options you can use to control the parser’s treatment of an XML document.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [XML Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparser)*