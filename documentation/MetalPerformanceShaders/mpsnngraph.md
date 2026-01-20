# MPSNNGraph

**Framework**: Metal Performance Shaders  
**Kind**: class

An optimized representation of a graph of neural network image and filter nodes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNGraph
```

#### Overview

Once you have prepared a graph of [`MPSNNImageNode`](mpsnnimagenode.md), [`MPSNNFilterNode`](mpsnnfilternode.md), and, if needed, [`MPSNNStateNode`](mpsnnstatenode.md) objects, you may initialize a [`MPSNNGraph`](mpsnngraph.md) using the image node that you wish to appear as the result. The graph object will introspect the graph representation and determine which nodes are needed for inputs, and which nodes are produced as output state (if any). Nodes which are not needed to calculate the result image node are ignored. Some nodes may be internally concatenated with other nodes for better performance.

> **Note**:  The [`MPSNNImageNode`](mpsnnimagenode.md) that you choose as the result node may be interior to a graph. This feature is provided as a means to examine intermediate computations in the full graph for debugging purposes.

During [`MPSNNGraph`](mpsnngraph.md) construction, the graph attached to the result node will be parsed and reduced to an optimized representation. This representation may be saved using the [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) protocol for later recall.

When decoding a [`MPSNNGraph`](mpsnngraph.md) using a [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder), it will be created against the system default [`MTLDevice`](https://developer.apple.com/documentation/Metal/MTLDevice). If you would like to set the device, your [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) should conform to the [`MPSDeviceProvider`](mpsdeviceprovider.md) protocol.

##### Debugging Tips

In typical usage, some refinement, especially of padding policies, may be required to get the expected answer from Metal Performance Shaders. If the result image is the wrong size, padding is typically the problem. When the answers are incorrect, the [`offset`](mpscnnkernel/offset.md) or other property may be incorrectly configured at some stage. As the graph is generated starting from an output image node, you may create other graphs starting at any image node within the graph. This will give you a view into the result produced from each intermediate layer with a minimum of fuss. In addition, the usual [`debugDescription()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/debugDescription()) method is available to inspect objects to make sure they conform to expectation.

Note that certain operations such as neuron filters that follow convolution filters and image concatenation may be optimized away by the [`MPSNNGraph`](mpsnngraph.md) when it is constructed. The convolution can do neuron operations as part of its operation. Concatenation is best done by writing the result of earlier filter passes in the right place using [`destinationFeatureChannelOffset`](mpscnnkernel/destinationfeaturechanneloffset.md) rather than by adding an extra copy. Other optimizations may be added as framework capabilities improve.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnngraph/init(coder:device:).md)
- [convenience init?(device: any MTLDevice, resultImage: MPSNNImageNode)](mpsnngraph/init(device:resultimage:).md)
- [init?(device: any MTLDevice, resultImage: MPSNNImageNode, resultImageIsNeeded: Bool)](mpsnngraph/init(device:resultimage:resultimageisneeded:).md)
- [init?(device: any MTLDevice, resultImages: [MPSNNImageNode], resultsAreNeeded: UnsafeMutablePointer<ObjCBool>?)](mpsnngraph/init(device:resultimages:resultsareneeded:).md)
### Instance Properties
- [var destinationImageAllocator: any MPSImageAllocator](mpsnngraph/destinationimageallocator.md)
- [protocol MPSImageAllocator](mpsimageallocator.md)
- [var intermediateImageHandles: [any MPSHandle]?](mpsnngraph/intermediateimagehandles.md)
- [var outputStateIsTemporary: Bool](mpsnngraph/outputstateistemporary.md)
- [var resultHandle: (any MPSHandle)?](mpsnngraph/resulthandle.md)
- [var resultStateHandles: [any MPSHandle]?](mpsnngraph/resultstatehandles.md)
- [var sourceImageHandles: [any MPSHandle]](mpsnngraph/sourceimagehandles.md)
- [var sourceStateHandles: [any MPSHandle]?](mpsnngraph/sourcestatehandles.md)
- [var format: MPSImageFeatureChannelFormat](mpsnngraph/format.md)
- [var resultImageIsNeeded: Bool](mpsnngraph/resultimageisneeded.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage]) -> MPSImage?](mpsnngraph/encode(to:sourceimages:).md)
- [func encode(to: any MTLCommandBuffer, sourceImages: [MPSImage], sourceStates: [MPSState]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> MPSImage?](mpsnngraph/encode(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [class MPSState](mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSNNBinaryGradientState](mpsnnbinarygradientstate.md)
  A class representing the state of a gradient binary kernel when it was encoded.
- [class MPSNNGradientState](mpsnngradientstate.md)
  A class representing the state of a gradient kernel when it was encoded.
- [func executeAsync(withSourceImages: [MPSImage], completionHandler: MPSNNGraphCompletionHandler) -> MPSImage](mpsnngraph/executeasync(withsourceimages:completionhandler:).md)
- [typealias MPSNNGraphCompletionHandler](mpsnngraphcompletionhandler.md)
  A notification when an asynchronous graph execution has finished.
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?) -> [MPSImage]?](mpsnngraph/encodebatch(to:sourceimages:sourcestates:).md)
- [func encodeBatch(to: any MTLCommandBuffer, sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, intermediateImages: NSMutableArray?, destinationStates: NSMutableArray?) -> [MPSImage]?](mpsnngraph/encodebatch(to:sourceimages:sourcestates:intermediateimages:destinationstates:).md)
- [func readCountForSourceImage(at: Int) -> Int](mpsnngraph/readcountforsourceimage(at:).md)
- [func readCountForSourceState(at: Int) -> Int](mpsnngraph/readcountforsourcestate(at:).md)
- [func reloadFromDataSources()](mpsnngraph/reloadfromdatasources.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSNNImageNode](mpsnnimagenode.md)
  A placeholder node denoting the position of a neural network image in a graph.
- [protocol MPSHandle](mpshandle.md)
  The protocol that provides resource identification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph)*