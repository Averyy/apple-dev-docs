# CGPSConverterEndDocumentCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Performs custom tasks at the end of a PostScript conversion process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias CGPSConverterEndDocumentCallback = (UnsafeMutableRawPointer?, Bool) -> Void
```

```c
typedef void (*)(void *, _Bool) CGPSConverterEndDocumentCallback;
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](./cgpsconverter/init%28info,callbacks,options%29.md).
- `success`: A Boolean value that indicates whether the PostScript conversion completed successfully ([`true`](../Swift/true.md) if it did).

## See Also

### Callbacks
- [CGPSConverterCallbacks](./cgpsconvertercallbacks.md)
  A structure for holding the callbacks provided when you create a PostScript converter object.
- [CGPSConverterBeginDocumentCallback](./cgpsconverterbegindocumentcallback.md)
  Performs custom tasks at the beginning of a PostScript conversion process.
- [CGPSConverterBeginPageCallback](./cgpsconverterbeginpagecallback.md)
  Performs custom tasks at the beginning of each page in a PostScript conversion process.
- [CGPSConverterEndPageCallback](./cgpsconverterendpagecallback.md)
  Performs custom tasks at the end of each page of a PostScript conversion process.
- [CGPSConverterProgressCallback](./cgpsconverterprogresscallback.md)
  Reports progress periodically during a PostScript conversion process.
- [CGPSConverterMessageCallback](./cgpsconvertermessagecallback.md)
  Passes messages generated during a PostScript conversion process.
- [CGPSConverterReleaseInfoCallback](./cgpsconverterreleaseinfocallback.md)
  Performs custom tasks when a PostScript converter is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterenddocumentcallback)*