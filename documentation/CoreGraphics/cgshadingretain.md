# CGShadingRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a shading object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern CGShadingRefCGShadingRetain(CGShadingRef shading);
```

#### Return Value

The same shading object you passed in as the `shading` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `shading` parameter is `NULL`.

## Parameters

- `shading`: The shading object to retain.

## See Also

### Retaining and Releasing Shading Objects
- [CGShadingRelease](./cgshadingrelease.md)
  Decrements the retain count of a shading object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgshadingretain)*