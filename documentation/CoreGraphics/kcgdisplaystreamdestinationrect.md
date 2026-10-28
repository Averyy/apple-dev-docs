# kCGDisplayStreamDestinationRect

**Framework**: Core Graphics  
**Kind**: var  
**Role**: Global Variable

## Declaration

```c
extern CFStringRef const kCGDisplayStreamDestinationRect;
```

## Discussion

This may be used to request where within the destination buffer the display updates should be placed. Use CGRectCreateDictionaryRepresentation to convert from a CGRect to the value used here.   Note: The coordinate system for the destination rectangle is always specified in output pixels to match the fact that the output buffer size is also specified in terms of pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamdestinationrect)*