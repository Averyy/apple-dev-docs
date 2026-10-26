# CFXMLParserGetStatusCode

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a numeric code indicating the current status of the parser.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLParserStatusCode CFXMLParserGetStatusCode(CFXMLParserRef parser);
```

#### Return Value

A status code indicating the current parser. See [`CFXMLParserStatusCode`](./cfxmlparserstatuscode.md) for a list of possible status codes.

#### Discussion

If an error has occurred, the code for the last error is returned. If no error has occurred, a status code is returned.

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
- [CFXMLParserGetSourceURL](./cfxmlparsergetsourceurl.md)
  Returns the URL for the XML data being parsed.
- [CFXMLParserGetTypeID](./cfxmlparsergettypeid.md)
  Returns the type identifier for the CFXMLParser opaque type.
- [CFXMLParserParse](./cfxmlparserparse.md)
  Begins a parse of the XML data that was associated with the parser when it was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparsergetstatuscode)*