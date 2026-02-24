# CGPSConverterEndDocumentCallback

**Framework**: Core Graphics  
**Kind**: typealias

Performs custom tasks at the end of a PostScript conversion process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias CGPSConverterEndDocumentCallback = (UnsafeMutableRawPointer?, Bool) -> Void
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](cgpsconverter/init(info:callbacks:options:).md).
- `success`: A Boolean value that indicates whether the PostScript conversion completed successfully ([`true`](https://developer.apple.com/documentation/Swift/true) if it did).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterenddocumentcallback)*