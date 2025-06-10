# transformationMatrixLayout

**Framework**: Metal  
**Kind**: property

Configures the layout for the transformation matrix in the transformation matrix buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var transformationMatrixLayout: MTLMatrixLayout { get set }
```

#### Discussion

You can provide matrices in column-major or row-major form, and this property allows you to control how Metal interprets them.

Defaults to `MTLMatrixLayoutColumnMajor`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/transformationmatrixlayout)*