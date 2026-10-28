# init(screenSize:label:)

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

A convenience initializer that creates a rate map descriptor with a given size and identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS

## Declaration

```swift
convenience init(screenSize: MTLSize, label: String? = nil)
```

## Return Value

A descriptor object whose [`screenSize`](./screensize.md) and [`label`](./label.md) properties are set to the provided values. You need to add at least one layer rate map to the descriptor.

## Parameters

- `screenSize`: The logical size, in pixels, of the viewport coordinate system.
- `label`: A string that identifies the resulting rate map.

## See Also

### Creating rate map descriptors
- [convenience init(screenSize: MTLSize, layer: MTLRasterizationRateLayerDescriptor, label: String?)](./init%28screensize,layer,label%29.md)
  A convenience initializer that creates a rate map descriptor with a single rate layer.
- [convenience init(screenSize: MTLSize, layers: [MTLRasterizationRateLayerDescriptor], label: String?)](./init%28screensize,layers,label%29.md)
  A convenience initializer that creates a rate map descriptor with a set of layer descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/init(screensize:label:))*