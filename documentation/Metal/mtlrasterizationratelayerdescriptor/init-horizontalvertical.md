# init(horizontal:vertical:)

**Framework**: Metal  
**Kind**: init

Initializes a layer rate map with a set of horizontal and vertical rasterization rates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
convenience init(horizontal: [Float], vertical: [Float])
```

#### Return Value

A layer descriptor whose width is the number of horizontal rates and whose height is the number of vertical rates. The layer descriptor copies the values from the input parameters.

## Parameters

- `horizontal`: An array of the horizontal rates to apply across the grid.
- `vertical`: An array of the vertical rates to apply across the grid.

## See Also

- [init(sampleCount: MTLSize)](mtlrasterizationratelayerdescriptor/init(samplecount:).md)
  Initializes the layer map with an empty grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/init(horizontal:vertical:))*