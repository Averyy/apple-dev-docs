# CGContextRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a graphics context.

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
extern CGContextRefCGContextRetain(CGContextRef c);
```

#### Return Value

The same graphics context you passed in as the `context` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except it does not cause an error if `c` is `NULL`.

## Parameters

- `c`: The graphics context to retain.

## See Also

### Retaining and Releasing Graphics Contexts
- [CGContextRelease](./cgcontextrelease.md)
  Decrements the retain count of a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextretain)*