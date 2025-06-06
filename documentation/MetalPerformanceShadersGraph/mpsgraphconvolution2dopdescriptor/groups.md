# groups

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The number of partitions of the input and output channels.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var groups: Int { get set }
```

#### Discussion

The convolution operation divides input and output channels in `groups` partitions. input channels in a group or partition are only connected to output channels in corresponding group. Number of weights the convolution needs is `outputFeatureChannels x inputFeatureChannels/groups x kernelWidth x kernelHeight`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/groups)*