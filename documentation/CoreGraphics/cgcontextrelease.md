# CGContextRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextRelease(CGContextRef c);
```

#### Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except it does not cause an error if `c` is `NULL`.

## Parameters

- `c`: The graphics context to release.

## See Also

### Retaining and Releasing Graphics Contexts
- [CGContextRetain](./cgcontextretain.md)
  Increments the retain count of a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextrelease)*