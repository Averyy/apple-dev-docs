# CGPSConverterProgressCallback

**Framework**: Core Graphics  
**Kind**: typealias

Reports progress periodically during a PostScript conversion process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias CGPSConverterProgressCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterprogresscallback)*