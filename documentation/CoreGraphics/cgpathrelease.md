# CGPathRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a graphics path.

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
extern void CGPathRelease(CGPathRef path);
```

#### Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `path` parameter is `NULL`.

## Parameters

- `path`: The graphics path to release.

## See Also

### Retaining and Releasing a Path
- [CGPathRetain](./cgpathretain.md)
  Increments the retain count of a graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathrelease)*