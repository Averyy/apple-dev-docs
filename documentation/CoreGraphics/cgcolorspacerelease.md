# CGColorSpaceRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a color space.

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
extern void CGColorSpaceRelease(CGColorSpaceRef space);
```

## Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `cs` parameter is `NULL`.

## Parameters

- `space`: The Quartz color space to release.

## See Also

### Retaining and Releasing Color Spaces
- [CGColorSpaceRetain](./cgcolorspaceretain.md)
  Increments the retain count of a color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspacerelease)*