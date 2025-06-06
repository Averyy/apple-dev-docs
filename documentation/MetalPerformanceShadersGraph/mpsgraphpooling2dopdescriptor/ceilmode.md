# ceilMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

Affects how the graph computes the output size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var ceilMode: Bool { get set }
```

#### Discussion

If set to `YES` then output size is computed by rounding up instead of down when dividing input size by stride. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling2dopdescriptor/ceilmode)*