# bidirectional

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that defines a bidirectional GRU layer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var bidirectional: Bool { get set }
```

#### Discussion

If set to `YES` then the input sequence is traversed in both directions and the two results are concatenated together on the channel-axis. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor/bidirectional)*