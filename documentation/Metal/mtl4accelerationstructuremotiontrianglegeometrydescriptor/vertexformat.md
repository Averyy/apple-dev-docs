# vertexFormat

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Defines the format of the vertices in the vertex buffers.

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

```objc
@property (nonatomic) MTLAttributeFormat vertexFormat;
```

## Discussion

All keyframes share the same vertex format. Defaults to `MTLAttributeFormatFloat3`, corresponding to three packed floating point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexformat)*