# vertexFormat

**Framework**: Metal  
**Kind**: property

Describes the format of the vertices in the vertex buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var vertexFormat: MTLAttributeFormat { get set }
```

#### Discussion

This property controls the format of the position attribute of the vertices the [`vertexBuffer`](mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer.md) references.

The format defaults to `MTLAttributeFormatFloat3`, corresponding to three packed floating point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat)*