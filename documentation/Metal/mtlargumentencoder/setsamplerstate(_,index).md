# setSamplerState(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a sampler into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setSamplerState(_ sampler: (any MTLSamplerState)?, index: Int)
```

```objc
- (void) setSamplerState:(id<MTLSamplerState>) sampler atIndex:(NSUInteger) index;
```

## Parameters

- `sampler`: A sampler the method encodes.
- `index`: The index of a sampler within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of an [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding samplers
- [func setSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./setsamplerstates%28_,range%29.md)
  Encodes an array of samplers into the argument buffer.
- [- setSamplerStates:withRange:](./setsamplerstates_withrange_.md)
  Encodes an array of samplers into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setsamplerstate(_:index:))*