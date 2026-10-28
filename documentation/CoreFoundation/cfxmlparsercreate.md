# CFXMLParserCreate

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new XML parser for the specified XML data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLParserRefCFXMLParserCreate(CFAllocatorRef allocator, CFDataRef xmlData, CFURLRef dataSource, CFOptionFlags parseOptions, CFIndex versionOfNodes, CFXMLParserCallBacks *callBacks, CFXMLParserContext *context);
```

## Return Value

The newly created parser. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `xmlData`: The XML data to parse. Do not pass `NULL`.
- `dataSource`: The URL from which the XML data was obtained. The URL is used to resolve any relative references found in XML Data. Pass `NULL` if a valid URL is unavailable.
- `parseOptions`: Flags which control how the XML data will be parsed. See [`CFXMLParserOptions`](./cfxmlparseroptions.md) for the list of available options.
- `versionOfNodes`: Determines which version of CFXMLNode objects are produced by the parser.
- `callBacks`: Callbacks called by the parser as the XML is processed. The callbacks are called as each XML tag is encountered, when an external entity needs to be resolved, and when an error occurs. See [`CFXMLParserCallBacks`](./cfxmlparsercallbacks.md) and the individual callbacks for more details. Do not pass `NULL`.
- `context`: Determines what, if any, information pointer is passed to the callbacks as the parse progresses; `context` may be `NULL`.

## See Also

### CFXMLParser Miscellaneous Functions
- [CFXMLParserAbort](./cfxmlparserabort.md)
  Causes a parser to abort with the given error code and description.
- [CFXMLParserCopyErrorDescription](./cfxmlparsercopyerrordescription.md)
  Returns the user-readable description of the current error condition.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparsercreate)*