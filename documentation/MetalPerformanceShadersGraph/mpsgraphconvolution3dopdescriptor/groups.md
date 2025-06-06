# groups

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The number of partitions of the input and output channels.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
var groups: Int { get set }
```

#### Discussion

The convolution operation divides input and output channels in `groups` partitions. input channels in a group or partition are only connected to output channels in corresponding group. Number of weights the convolution needs is `outputFeatureChannels x inputFeatureChannels/groups x kernelDepth x kernelWidth x kernelHeight`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/groups)*