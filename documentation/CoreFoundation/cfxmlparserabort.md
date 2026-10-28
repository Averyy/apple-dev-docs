# CFXMLParserAbort

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Causes a parser to abort with the given error code and description.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern void CFXMLParserAbort(CFXMLParserRef parser, CFXMLParserStatusCode errorCode, CFStringRef errorDescription);
```

## Discussion

This function cannot be called asynchronously. In other words, it must be called from within a parser callback function.

## Parameters

- `parser`: The parser to abort.
- `errorCode`: The error code to return to the parser.
- `errorDescription`: The error description string to return to the parser. This value may not be `NULL`.

## See Also

### CFXMLParser Miscellaneous Functions
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparserabort)*