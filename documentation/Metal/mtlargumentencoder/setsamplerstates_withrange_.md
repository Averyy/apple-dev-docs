# setSamplerStates:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes an array of samplers into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setSamplerStates:(id<MTLSamplerState> const[]) samplers withRange:(NSRange) range;
```

## Parameters

- `samplers`: An array of samplers the method encodes.
- `range`: A range of indices within the argument buffer for each element in `samplers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding samplers
- [func setSamplerState((any MTLSamplerState)?, index: Int)](./setsamplerstate%28_,index%29.md)
  Encodes a sampler into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setsamplerstates:withrange:)*