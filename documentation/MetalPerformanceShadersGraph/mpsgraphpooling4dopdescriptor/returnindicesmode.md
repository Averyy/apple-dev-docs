# returnIndicesMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

Defines the mode for returned indices of maximum values within each pooling window.

**Availability**:
- iOS 15.3+
- iPadOS 15.3+
- Mac Catalyst 15.3+
- macOS 12.2+
- tvOS 15.3+
- visionOS 1.0+

## Declaration

```swift
var returnIndicesMode: MPSGraphPoolingReturnIndicesMode { get set }
```

#### Discussion

Use this in conjunction with [`maxPooling4DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling4dreturnindices(_:descriptor:name:).md) API. If `returnIndicesMode = MPSGraphPoolingReturnIndicesNone` then only the first result MPSGraph returns from [`maxPooling4DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling4dreturnindices(_:descriptor:name:).md) will be valid and using the second result will assert. Default value: `MPSGraphPoolingReturnIndicesNone`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/returnindicesmode)*