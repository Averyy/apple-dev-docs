# CGPSConverterMessageCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Passes messages generated during a PostScript conversion process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias CGPSConverterMessageCallback = (UnsafeMutableRawPointer?, CFString) -> Void
```

```c
typedef void (*)(void *, const struct __CFString *) CGPSConverterMessageCallback;
```

#### Discussion

There are several kinds of message that might be sent during a conversion process. The most likely are font substitution messages, and any messages that the PostScript code itself generates. Any PostScript messages written to `stdout` are routed through this callback—typically these are debugging or status messages and, although uncommon, can be useful in debugging. In addition, there may be error messages if the document is malformed.

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](./cgpsconverter/init%28info,callbacks,options%29.md).
- `message`: A string containing the message from the PostScript conversion process.

## See Also

### Callbacks
- [CGPSConverterCallbacks](./cgpsconvertercallbacks.md)
  A structure for holding the callbacks provided when you create a PostScript converter object.
- [CGPSConverterBeginDocumentCallback](./cgpsconverterbegindocumentcallback.md)
  Performs custom tasks at the beginning of a PostScript conversion process.
- [CGPSConverterEndDocumentCallback](./cgpsconverterenddocumentcallback.md)
  Performs custom tasks at the end of a PostScript conversion process.
- [CGPSConverterBeginPageCallback](./cgpsconverterbeginpagecallback.md)
  Performs custom tasks at the beginning of each page in a PostScript conversion process.
- [CGPSConverterEndPageCallback](./cgpsconverterendpagecallback.md)
  Performs custom tasks at the end of each page of a PostScript conversion process.
- [CGPSConverterProgressCallback](./cgpsconverterprogresscallback.md)
  Reports progress periodically during a PostScript conversion process.
- [CGPSConverterReleaseInfoCallback](./cgpsconverterreleaseinfocallback.md)
  Performs custom tasks when a PostScript converter is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconvertermessagecallback)*