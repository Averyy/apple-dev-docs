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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterenddocumentcallback)*