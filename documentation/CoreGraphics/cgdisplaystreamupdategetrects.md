# CGDisplayStreamUpdateGetRects

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern const CGRect *CGDisplayStreamUpdateGetRects(CGDisplayStreamUpdateRef updateRef, CGDisplayStreamUpdateRectType rectType, size_t *rectCount);
```

#### Return Value

A pointer to the array of CGRectangles.  This array should not be freed by the caller.

#### Discussion

Returns a pointer to an array of CGRect structs that describe what parts of the frame have changed relative to the previously delivered frame.   This rectangle list encapsulates both the update rectangles and movement rectangles.

## Parameters

- `updateRef`: The CGDisplayStreamUpdateRef
- `rectCount`: A pointer to where the count of the number of rectangles in the array is to be returned. Must not be NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdategetrects)*