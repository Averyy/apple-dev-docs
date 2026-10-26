# CGDisplayStreamStop

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern CGError CGDisplayStreamStop(CGDisplayStreamRef displayStream);
```

#### Return Value

kCGErrorSuccess If the display stream was stopped, otherwise an error.

#### Discussion

End delivery of frame updates to the handler block.

After this call returns, the CGDisplayStream callback function will eventually be called with a status of kCGDisplayStreamFrameStatusStopped.  After that point it is safe to release the CGDisplayStream. It is safe to call this function from within the handler block, but the previous caveat still applies.

## Parameters

- `displayStream`: To be stopped


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamstop)*