# CGLayerRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a layer object.

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
extern CGLayerRefCGLayerRetain(CGLayerRef layer);
```

#### Return Value

The same layer you passed in as the `layer` parameter.

#### Discussion

This function is equivalent to calling [`CFRetain`](../CoreFoundation/cfretain.md) except that it does not crash if the `layer` parameter is `null`.

## Parameters

- `layer`: The layer to retain.

## See Also

### Retaining and Releasing Color Objects
- [CGLayerRelease](./cglayerrelease.md)
  Decrements the retain count of a layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglayerretain)*