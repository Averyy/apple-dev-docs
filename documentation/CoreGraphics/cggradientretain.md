# CGGradientRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a CGGradient object.

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
extern CGGradientRefCGGradientRetain(CGGradientRef gradient);
```

#### Return Value

The same gradient object that you passed in as the `gradient` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `gradient` parameter is `NULL`.

## Parameters

- `gradient`: The gradient object to retain.

## See Also

### Retaining and Releasing a Gradient
- [CGGradientRelease](./cggradientrelease.md)
  Decrements the retain count of a CGGradient object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradientretain)*