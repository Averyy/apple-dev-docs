# CFXMLParserGetSourceURL

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the URL for the XML data being parsed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFURLRefCFXMLParserGetSourceURL(CFXMLParserRef parser);
```

## Return Value

The URL for the XML document being parsed. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `parser`: The XML parser to examine.

## See Also

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
- [CFXMLParserGetStatusCode](./cfxmlparsergetstatuscode.md)
  Returns a numeric code indicating the current status of the parser.
- [CFXMLParserGetTypeID](./cfxmlparsergettypeid.md)
  Returns the type identifier for the CFXMLParser opaque type.
- [CFXMLParserParse](./cfxmlparserparse.md)
  Begins a parse of the XML data that was associated with the parser when it was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparsergetsourceurl)*