# transformationMatrixLayout

**Framework**: Metal  
**Kind**: property

Configures the layout for the transformation matrix in the transformation matrix buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var transformationMatrixLayout: MTLMatrixLayout { get set }
```

#### Discussion

You can provide matrices in column-major or row-major form, and this property allows you to control how Metal interprets them.

Defaults to `MTLMatrixLayoutColumnMajor`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuretrianglegeometrydescriptor/transformationmatrixlayout)*