# PGDisplayNewFrameEventHandler

**Framework**: Paravirtualized Graphics  
**Kind**: typealias  
**Role**: Type Alias

The block signature for a routine that handles frame updates from the guest.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGDisplayNewFrameEventHandler = () -> Void
```

```c
typedef void (^)(void) PGDisplayNewFrameEventHandler;
```

## See Also

### Handling Frame Events
- [var newFrameEventHandler: PGDisplayNewFrameEventHandler?](./pgdisplaydescriptor/newframeeventhandler.md)
  A handler that the framework calls when the guest environment has a new frame to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaynewframeeventhandler)*