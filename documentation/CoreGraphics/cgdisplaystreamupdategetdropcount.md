# CGDisplayStreamUpdateGetDropCount

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern size_t CGDisplayStreamUpdateGetDropCount(CGDisplayStreamUpdateRef updateRef);
```

#### Return Value

The number of dropped frames

#### Discussion

Return how many frames (if any) have been dropped since the last call to the handler.

This call is primarily useful for performance measurement to determine if the client is keeping up with all WindowServer updates.

## Parameters

- `updateRef`: The CGDisplayStreamUpdateRef


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdategetdropcount)*