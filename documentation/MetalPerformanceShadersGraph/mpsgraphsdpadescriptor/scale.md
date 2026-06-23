# scale

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scale applied to the result of the query–key matrix multiply before softmax. Typically set to `1/sqrt(headDimension)`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var scale: Float { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/scale)*