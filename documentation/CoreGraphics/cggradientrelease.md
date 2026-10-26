# CGGradientRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a CGGradient object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGGradientRelease(CGGradientRef gradient);
```

#### Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `gradient` parameter is `NULL`.

## Parameters

- `gradient`: The gradient object to release.

## See Also

### Retaining and Releasing a Gradient
- [CGGradientRetain](./cggradientretain.md)
  Increments the retain count of a CGGradient object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradientrelease)*