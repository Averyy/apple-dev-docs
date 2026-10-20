# CGPSConverterBeginDocumentCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Performs custom tasks at the beginning of a PostScript conversion process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias CGPSConverterBeginDocumentCallback = (UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(void *) CGPSConverterBeginDocumentCallback;
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](./cgpsconverter/init%28info,callbacks,options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterbegindocumentcallback)*