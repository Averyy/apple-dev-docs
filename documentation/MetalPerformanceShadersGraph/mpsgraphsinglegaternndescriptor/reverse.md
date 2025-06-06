# reverse

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that defines time direction of the input sequence.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
var reverse: Bool { get set }
```

#### Discussion

If set to `YES` then the input sequence is passed in reverse time order to the layer. Note: Ignored when `bidirectional = YES`. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsinglegaternndescriptor/reverse)*