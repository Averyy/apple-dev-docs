# CGPSConverterBeginDocumentCallback

**Framework**: Core Graphics  
**Kind**: typealias

Performs custom tasks at the beginning of a PostScript conversion process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias CGPSConverterBeginDocumentCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterbegindocumentcallback)*