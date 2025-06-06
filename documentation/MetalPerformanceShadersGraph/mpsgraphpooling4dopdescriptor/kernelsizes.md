# kernelSizes

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

Defines the pooling window size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var kernelSizes: [NSNumber] { get set }
```

#### Discussion

Must be four numbers, one for each spatial dimension, fastest running index last.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/kernelsizes)*