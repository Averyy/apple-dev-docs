# CGColorRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a color.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern CGColorRefCGColorRetain(CGColorRef color);
```

#### Return Value

The same color you passed in as the `color` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `color` parameter is `NULL`.

## Parameters

- `color`: The color to retain.

## See Also

### Retaining and Releasing Color Objects
- [CGColorRelease](./cgcolorrelease.md)
  Decrements the retain count of a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorretain)*