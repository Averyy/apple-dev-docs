# kCGDisplayStreamSourceRect

**Framework**: Core Graphics  
**Kind**: var  
**Role**: Global Variable

## Declaration

```c
extern CFStringRef const kCGDisplayStreamSourceRect;
```

#### Discussion

This may be used to request a subregion of the display to be provided as the source of the display stream.  Use CGRectCreateDictionaryRepresentation to convert from a CGRect to the value used here.   Note: The coordinate system for the source rectangle is specified in display logical coordinates and not in pixels, in order to match the normal convention on HiDPI displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamsourcerect)*