# vertexFormat

**Framework**: Metal  
**Kind**: property

Defines the format of the vertices in the vertex buffers.

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

All keyframes share the same vertex format. Defaults to `MTLAttributeFormatFloat3`, corresponding to three packed floating point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexformat)*