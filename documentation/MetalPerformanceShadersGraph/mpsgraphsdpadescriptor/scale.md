# scale

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scale applied to the result of the query–key matrix multiply before softmax. Typically set to `1/sqrt(headDimension)`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var scale: Float { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/scale)*