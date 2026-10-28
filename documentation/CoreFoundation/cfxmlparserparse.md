# CFXMLParserParse

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Begins a parse of the XML data that was associated with the parser when it was created.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern Boolean CFXMLParserParse(CFXMLParserRef parser);
```

## Return Value

`true` if the parse was successful, `false` otherwise.

## Discussion

Upon success, use the [`CFXMLParserGetDocument`](./cfxmlparsergetdocument.md) function to get the product of the parse. Upon failure, use the [`CFXMLParserGetContext`](./cfxmlparsergetcontext.md) or [`CFXMLParserCopyErrorDescription`](./cfxmlparsercopyerrordescription.md) functions to get information about the error. It is an error to call the [`CFXMLParserParse`](./cfxmlparserparse.md) function while a parse is already underway.

## Parameters

- `parser`: The XML parser to start.

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
- [CFXMLParserGetStatusCode](./cfxmlparsergetstatuscode.md)
  Returns a numeric code indicating the current status of the parser.
- [CFXMLParserGetTypeID](./cfxmlparsergettypeid.md)
  Returns the type identifier for the CFXMLParser opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparserparse)*