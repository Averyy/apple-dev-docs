# training

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that enables the LSTM layer to support training.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
var training: Bool { get set }
```

#### Discussion

If set to `YES` then the layer will produce training state tensor as a secondary output. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlstmdescriptor/training)*