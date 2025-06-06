# PGDisplayNewFrameEventHandler

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that handles frame updates from the guest.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGDisplayNewFrameEventHandler = () -> Void
```

## See Also

- [var newFrameEventHandler: PGDisplayNewFrameEventHandler?](pgdisplaydescriptor/newframeeventhandler.md)
  A handler that the framework calls when the guest environment has a new frame to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaynewframeeventhandler)*