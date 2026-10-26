# CGDisplayStreamGetRunLoopSource

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern CFRunLoopSourceRefCGDisplayStreamGetRunLoopSource(CGDisplayStreamRef displayStream);
```

#### Return Value

The CFRunLoopSource for this displayStream.  Note: This function will return NULL if the display stream was created via  CGDisplayStreamCreateWithDispatchQueue().

#### Discussion

Return the singleton CFRunLoopSourceRef for a CGDisplayStream.

## Parameters

- `displayStream`: The CGDisplayStream object


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamgetrunloopsource)*