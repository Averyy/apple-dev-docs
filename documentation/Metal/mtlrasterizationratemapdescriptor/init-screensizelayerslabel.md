# init(screenSize:layers:label:)

**Framework**: Metal  
**Kind**: init

A convenience initializer that creates a rate map descriptor with a set of layer descriptors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
convenience init(screenSize: MTLSize, layers: [MTLRasterizationRateLayerDescriptor], label: String? = nil)
```

#### Return Value

A descriptor object whose [`screenSize`](mtlrasterizationratemapdescriptor/screensize.md) and [`label`](mtlrasterizationratemapdescriptor/label.md) properties are set to the provided values and whose rate map layers are set to the array you provided.

## Parameters

- `screenSize`: The logical size, in pixels, of the viewport coordinate system.
- `layers`: An array of rate layer descriptors for the rate map’s layers.
- `label`: A string that identifies the resulting rate map.

## See Also

- [convenience init(screenSize: MTLSize, label: String?)](mtlrasterizationratemapdescriptor/init(screensize:label:).md)
  A convenience initializer that creates a rate map descriptor with a given size and identifier.
- [convenience init(screenSize: MTLSize, layer: MTLRasterizationRateLayerDescriptor, label: String?)](mtlrasterizationratemapdescriptor/init(screensize:layer:label:).md)
  A convenience initializer that creates a rate map descriptor with a single rate layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/init(screensize:layers:label:))*