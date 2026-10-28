# CFXMLParser

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS

## Declaration

```swift
class CFXMLParser
```

```c
typedef struct __CFXMLParser * CFXMLParserRef;
```

## Overview

CFXMLParser provides an XML parser you can use to find and extract data in XML documents. You can use a high-level interface to load an XML document into a Core Foundation collection object. A low-level callback-based interface allows you to perform any action you wish on an XML structured type when it is detected by the parser. This opaque type is relevant for applications that need information about an XML document’s structure or content.

## Topics

### Callbacks
- [typealias CFXMLParserAddChildCallBack](./cfxmlparseraddchildcallback.md)
  Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [typealias CFXMLParserCopyDescriptionCallBack](./cfxmlparsercopydescriptioncallback.md)
  Callback function invoked by the parser when handling the information pointer.
- [typealias CFXMLParserCreateXMLStructureCallBack](./cfxmlparsercreatexmlstructurecallback.md)
  Callback function invoked when the parser encounters an XML open tag.
- [typealias CFXMLParserEndXMLStructureCallBack](./cfxmlparserendxmlstructurecallback.md)
  Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.
- [typealias CFXMLParserHandleErrorCallBack](./cfxmlparserhandleerrorcallback.md)
  Callback function invoked by the parser to notify your application that an error has occurred.
- [typealias CFXMLParserReleaseCallBack](./cfxmlparserreleasecallback.md)
  Callback function invoked by the parser when it wants to release a reference to the information pointer.
- [typealias CFXMLParserResolveExternalEntityCallBack](./cfxmlparserresolveexternalentitycallback.md)
  Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [typealias CFXMLParserRetainCallBack](./cfxmlparserretaincallback.md)
  Callback function invoked by the parser when it needs another reference to the information pointer.
### Data Types
- [struct CFXMLParserCallBacks](./cfxmlparsercallbacks.md)
  Contains version information and function pointers to callbacks needed when parsing XML.
- [struct CFXMLParserContext](./cfxmlparsercontext.md)
  Contains version information and function pointers to callbacks used when handling a program-defined context.
### Constants
- [struct CFXMLParserStatusCode](./cfxmlparserstatuscode.md)
  The various status and error flags that can be returned by the parser.
- [struct CFXMLParserOptions](./cfxmlparseroptions.md)
  Options you can use to control the parser’s treatment of an XML document.
### CFXMLParser Miscellaneous Functions
- [CFXMLParserAbort](./cfxmlparserabort.md)
  Causes a parser to abort with the given error code and description.
- [CFXMLParserCopyErrorDescription](./cfxmlparsercopyerrordescription.md)
  Returns the user-readable description of the current error condition.
- [CFXMLParserCreate](./cfxmlparsercreate.md)
  Creates a new XML parser for the specified XML data.
- [CFXMLParserCreateWithDataFromURL](./cfxmlparsercreatewithdatafromurl.md)
  Creates a new XML parser for the specified XML data at the specified URL.
- [CFXMLParserGetCallBacks](./cfxmlparsergetcallbacks.md)
  Returns the callbacks associated with an XML parser when it was created.
- [CFXMLParserGetContext](./cfxmlparsergetcontext.md)
  Returns the context for an XML parser.
- [CFXMLParserGetDocument](./cfxmlparsergetdocument.md)
  Returns the top-most object returned by the create XML structure callback.
- [CFXMLParserGetLineNumber](./cfxmlparsergetlinenumber.md)
  Returns the line number of the current parse location.
- [CFXMLParserGetLocation](./cfxmlparsergetlocation.md)
  Returns the character index of the current parse location.
- [CFXMLParserGetSourceURL](./cfxmlparsergetsourceurl.md)
  Returns the URL for the XML data being parsed.
- [CFXMLParserGetStatusCode](./cfxmlparsergetstatuscode.md)
  Returns a numeric code indicating the current status of the parser.
- [CFXMLParserGetTypeID](./cfxmlparsergettypeid.md)
  Returns the type identifier for the CFXMLParser opaque type.
- [CFXMLParserParse](./cfxmlparserparse.md)
  Begins a parse of the XML data that was associated with the parser when it was created.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [XML Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparser)*