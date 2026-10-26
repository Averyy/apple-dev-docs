# MPSNNImageNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A placeholder node denoting the position of a neural network image in a graph.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNImageNode
```

```objc
@interface MPSNNImageNode : NSObject
```

## Topics

### Initializers
- [init(handle: (any MPSHandle)?)](./mpsnnimagenode/init%28handle%29.md)
### Instance Properties
- [var exportFromGraph: Bool](./mpsnnimagenode/exportfromgraph.md)
- [var format: MPSImageFeatureChannelFormat](./mpsnnimagenode/format.md)
- [enum MPSImageFeatureChannelFormat](./mpsimagefeaturechannelformat.md)
  Encodes the representation of a single channel within an image.
- [var handle: (any MPSHandle)?](./mpsnnimagenode/handle.md)
- [var imageAllocator: any MPSImageAllocator](./mpsnnimagenode/imageallocator.md)
- [var stopGradient: Bool](./mpsnnimagenode/stopgradient.md)
- [var synchronizeResource: Bool](./mpsnnimagenode/synchronizeresource.md)
### Type Methods
- [class func exportedNode(with: (any MPSHandle)?) -> Self](./mpsnnimagenode/exportednode%28with%29.md)
- [+ nodeWithHandle:](./mpsnnimagenode/nodewithhandle_.md)
### Supporting Types
- [protocol MPSHandle](./mpshandle.md)
  The protocol that provides resource identification.
- [enum MPSImageFeatureChannelFormat](./mpsimagefeaturechannelformat.md)
  Encodes the representation of a single channel within an image.
- [protocol MPSImageAllocator](./mpsimageallocator.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Neural Network Graphs
- [class MPSNNGraph](./mpsnngraph.md)
  An optimized representation of a graph of neural network image and filter nodes.
- [protocol MPSHandle](./mpshandle.md)
  The protocol that provides resource identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnimagenode)*