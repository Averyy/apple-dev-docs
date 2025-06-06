# PGDisplayModeChangeHandler

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that handles changes to the display’s graphics mode.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGDisplayModeChangeHandler = (PGDisplayCoord_t, OSType) -> Void
```

## Parameters

- `sizeInPixels`: The dimensions of the new display mode.
- `pixelFormat`: The pixel format of the new display mode.

## See Also

- [var modeChangeHandler: PGDisplayModeChangeHandler?](pgdisplaydescriptor/modechangehandler.md)
  A handler that the framework calls to change the virtual display’s graphics mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaymodechangehandler)*