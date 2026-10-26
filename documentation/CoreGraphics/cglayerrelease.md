# CGLayerRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a layer object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGLayerRelease(CGLayerRef layer);
```

#### Discussion

This function is equivalent to calling [`CFRelease`](../CoreFoundation/cfrelease.md) except that it does not crash if the `layer` parameter is `null`.

## Parameters

- `layer`: The layer to release.

## See Also

### Retaining and Releasing Color Objects
- [CGLayerRetain](./cglayerretain.md)
  Increments the retain count of a layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglayerrelease)*