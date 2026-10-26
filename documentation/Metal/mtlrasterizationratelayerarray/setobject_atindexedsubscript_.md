# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Stores a sample value at the specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLRasterizationRateLayerDescriptor *) layer atIndexedSubscript:(NSUInteger) layerIndex;
```

#### Discussion

The method converts the value to a single precision floating point value.

## Parameters

- `layer`: The layer descriptor to set
- `layerIndex`: The index of the sample you want to set.

## See Also

### Accessing members of the array
- [subscript(Int) -> MTLRasterizationRateLayerDescriptor?](./subscript%28_%29.md)
  Retrieves the sample value at the specified index.
- [class MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)
  The minimum rasterization rates to apply to sections of a layer in the render target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerarray/setobject:atindexedsubscript:)*