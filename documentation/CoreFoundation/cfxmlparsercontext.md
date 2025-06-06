# CFXMLParserContext

**Framework**: Core Foundation  
**Kind**: struct

Contains version information and function pointers to callbacks used when handling a program-defined context.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLParserContext
```

#### Overview

You can associate a context with a parser when the parser is created. The context can be anything you wish and will be passed as a parameter to all of the XML parser callbacks.

## Topics

### Initializers
- [init()](cfxmlparsercontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: CFXMLParserRetainCallBack!, release: CFXMLParserReleaseCallBack!, copyDescription: CFXMLParserCopyDescriptionCallBack!)](cfxmlparsercontext/init(version:info:retain:release:copydescription:).md)
### Instance Properties
- [var copyDescription: CFXMLParserCopyDescriptionCallBack!](cfxmlparsercontext/copydescription.md)
  A copy description callback for your program-defined context data. Optional.
- [var info: UnsafeMutableRawPointer!](cfxmlparsercontext/info.md)
  An arbitrary program-defined value passed to all the callbacks in this structure and in the [`CFXMLParserCallBacks`](cfxmlparsercallbacks.md) structure.
- [var release: CFXMLParserReleaseCallBack!](cfxmlparsercontext/release.md)
  A release callback for your program-defined context data. Optional.
- [var retain: CFXMLParserRetainCallBack!](cfxmlparsercontext/retain.md)
  A retain callback for your program-defined context data. Optional.
- [var version: CFIndex](cfxmlparsercontext/version.md)
  Version number of this structure. Must be 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct CFXMLParserCallBacks](cfxmlparsercallbacks.md)
  Contains version information and function pointers to callbacks needed when parsing XML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparsercontext)*