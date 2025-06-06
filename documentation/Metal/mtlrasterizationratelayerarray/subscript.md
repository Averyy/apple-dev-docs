# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Retrieves the sample value at the specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(layerIndex: Int) -> MTLRasterizationRateLayerDescriptor? { get set }
```

#### Return Value

An [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) instance describing the value of the sample at the specified index, or `0` if the index is out of range.

## Parameters

- `layerIndex`: The index of the sample you want to retrieve.

## See Also

- [class MTLRasterizationRateLayerDescriptor](mtlrasterizationratelayerdescriptor.md)
  The minimum rasterization rates to apply to sections of a layer in the render target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerarray/subscript(_:))*