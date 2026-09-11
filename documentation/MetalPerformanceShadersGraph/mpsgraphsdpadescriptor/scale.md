# scale

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scale applied to the result of the query–key matrix multiply before softmax. Typically set to `1/sqrt(headDimension)`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var scale: Float { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/scale)*