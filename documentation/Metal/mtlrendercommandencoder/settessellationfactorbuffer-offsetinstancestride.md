# setTessellationFactorBuffer(_:offset:instanceStride:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the per-patch tessellation factors for any subsequent patch-drawing commands.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setTessellationFactorBuffer(_ buffer: (any MTLBuffer)?, offset: Int, instanceStride: Int)
```

#### Discussion

Call this method before encoding patch-drawing commands.

## Parameters

- `buffer`: An   instance that stores the per-patch tessellation factors, which can’t be empty or  .
- `offset`: The distance, in bytes, between the start of the data and the start of the buffer, which needs to be a multiple of  .
- `instanceStride`: The number of bytes between two instances of data in  , which needs to be a multiple of  .

## See Also

- [func setTessellationFactorScale(Float)](mtlrendercommandencoder/settessellationfactorscale(_:).md)
  Configures the scale factor for per-patch tessellation factors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settessellationfactorbuffer(_:offset:instancestride:))*