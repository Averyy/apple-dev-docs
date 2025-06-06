# setTessellationFactorScale(_:)

**Framework**: Metal  
**Kind**: method  
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

#### Discussion

The command converts `scale` to a half-precision floating-point value before it applies it to the per-patch tessellation factors (see [`setTessellationFactorBuffer(_:offset:instanceStride:)`](mtlrendercommandencoder/settessellationfactorbuffer(_:offset:instancestride:).md)).

## Parameters

- `scale`: The value of   can’t be negative, infinite, equal to   (not a number), or a denormalized number.

## See Also

- [func setTessellationFactorBuffer((any MTLBuffer)?, offset: Int, instanceStride: Int)](mtlrendercommandencoder/settessellationfactorbuffer(_:offset:instancestride:).md)
  Configures the per-patch tessellation factors for any subsequent patch-drawing commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settessellationfactorscale(_:))*