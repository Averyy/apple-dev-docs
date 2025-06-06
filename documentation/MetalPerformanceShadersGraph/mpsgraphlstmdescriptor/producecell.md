# produceCell

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that controls whether or not to return the output cell from the LSTM layer.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
var produceCell: Bool { get set }
```

#### Discussion

If set to `YES` then this layer will produce the internal cell of the LSTM unit as secondary output. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlstmdescriptor/producecell)*