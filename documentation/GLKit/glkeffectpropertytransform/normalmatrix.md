# normalMatrix

**Framework**: GLKit  
**Kind**: property

The matrix used to transform normal coordinates from world space to eye space.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var normalMatrix: GLKMatrix3 { get }
```

#### Discussion

The normal matrix is derived from the [`modelviewMatrix`](glkeffectpropertytransform/modelviewmatrix.md) property and is automatically calculated when needed.

## See Also

- [var modelviewMatrix: GLKMatrix4](glkeffectpropertytransform/modelviewmatrix.md)
  The matrix used to transform position coordinates from world space to eye space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform/normalmatrix)*