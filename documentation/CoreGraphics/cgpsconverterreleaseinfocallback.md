# CGPSConverterReleaseInfoCallback

**Framework**: Core Graphics  
**Kind**: typealias

Performs custom tasks when a PostScript converter is released.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias CGPSConverterReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](cgpsconverter/init(info:callbacks:options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterreleaseinfocallback)*