# CGPSConverterReleaseInfoCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Performs custom tasks when a PostScript converter is released.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias CGPSConverterReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(void *) CGPSConverterReleaseInfoCallback;
```

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:callbacks:options:)`](./cgpsconverter/init%28info,callbacks,options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpsconverterreleaseinfocallback)*