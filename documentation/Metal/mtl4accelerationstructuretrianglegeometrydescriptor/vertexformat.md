# vertexFormat

**Framework**: Metal  
**Kind**: property

Describes the format of the vertices in the vertex buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var vertexFormat: MTLAttributeFormat { get set }
```

#### Discussion

This property controls the format of the position attribute of the vertices the [`vertexBuffer`](mtl4accelerationstructuretrianglegeometrydescriptor/vertexbuffer.md) references.

The format defaults to `MTLAttributeFormatFloat3`, corresponding to three packed floating point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/vertexformat)*