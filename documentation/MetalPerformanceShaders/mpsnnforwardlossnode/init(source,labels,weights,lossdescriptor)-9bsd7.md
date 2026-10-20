# init(source:labels:weights:lossDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(source: MPSNNImageNode, labels: MPSNNImageNode, weights: MPSNNImageNode, lossDescriptor descriptor: MPSCNNLossDescriptor)
```

```objc
+ (instancetype) nodeWithSource:(MPSNNImageNode *) source labels:(MPSNNImageNode *) labels weights:(MPSNNImageNode *) weights lossDescriptor:(MPSCNNLossDescriptor *) descriptor;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardlossnode/init(source:labels:weights:lossdescriptor:)-9bsd7)*