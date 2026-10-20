# MPSRNNDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A description of a recursive neural network block or layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNDescriptor
```

```objc
@interface MPSRNNDescriptor : NSObject
```

## Topics

### Instance Properties
- [var inputFeatureChannels: Int](./mpsrnndescriptor/inputfeaturechannels.md)
- [var layerSequenceDirection: MPSRNNSequenceDirection](./mpsrnndescriptor/layersequencedirection.md)
- [var outputFeatureChannels: Int](./mpsrnndescriptor/outputfeaturechannels.md)
- [var useFloat32Weights: Bool](./mpsrnndescriptor/usefloat32weights.md)
- [var useLayerInputUnitTransformMode: Bool](./mpsrnndescriptor/uselayerinputunittransformmode.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPSGRUDescriptor](./mpsgrudescriptor.md)
- [MPSLSTMDescriptor](./mpslstmdescriptor.md)
- [MPSRNNSingleGateDescriptor](./mpsrnnsinglegatedescriptor.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsrnnimageinferencelayer/init%28coder,device%29.md)
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor)](./mpsrnnimageinferencelayer/init%28device,rnndescriptor%29.md)
- [init(device: any MTLDevice, rnnDescriptors: [MPSRNNDescriptor])](./mpsrnnimageinferencelayer/init%28device,rnndescriptors%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnndescriptor)*