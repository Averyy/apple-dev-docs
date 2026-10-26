# kCGDisplayStreamPreserveAspectRatio

**Framework**: Core Graphics  
**Kind**: var  
**Role**: Global Variable

## Declaration

```c
extern CFStringRef const kCGDisplayStreamPreserveAspectRatio;
```

#### Discussion

Enable/disable the work the Window Server will do to preserve the display aspect ratio.  By default the Window Server will assume that it should preserve the original aspect ratio of the source display rect.  If the aspect ratio of the source display and the display stream destination rect are not the same, black borders will be inserted at the top/bottom or right/left sides of the destination in order to preserve the source aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgdisplaystreampreserveaspectratio)*