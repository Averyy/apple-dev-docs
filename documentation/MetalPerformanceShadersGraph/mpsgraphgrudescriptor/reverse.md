# reverse

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that defines the time direction of the input sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var reverse: Bool { get set }
```

#### Discussion

If set to `YES` then the input sequence is passed in reverse time order to the layer. Note: Ignored when `bidirectional = YES`. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor/reverse)*