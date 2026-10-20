# setTessellationFactorScale(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Configures the scale factor for per-patch tessellation factors.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setTessellationFactorScale(_ scale: Float)
```

```objc
- (void) setTessellationFactorScale:(float) scale;
```

#### Discussion

The command converts `scale` to a half-precision floating-point value before it applies it to the per-patch tessellation factors (see [`setTessellationFactorBuffer(_:offset:instanceStride:)`](./settessellationfactorbuffer%28_,offset,instancestride%29.md)).

## Parameters

- `scale`: A positive, normal floating-point scale factor the render pass applies to the per-patch tessellation factors.

  The value of `scale` can’t be negative, infinite, equal to `NaN` (not a number), or a denormalized number.

## See Also

### Configuring tessellation factors
- [func setTessellationFactorBuffer((any MTLBuffer)?, offset: Int, instanceStride: Int)](./settessellationfactorbuffer%28_,offset,instancestride%29.md)
  Configures the per-patch tessellation factors for any subsequent patch-drawing commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settessellationfactorscale(_:))*