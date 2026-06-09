# CanaryDescription

**Framework**: RealityKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class CanaryDescription
```

## Topics

### Creating a description
- [init(multipliers: _Proto_LowLevelDeformationDescription_v1.Buffer, options: _Proto_LowLevelDeformationDescription_v1.SemanticOptions, modulus: Int, moduloOffset: Int)](canarydescription/init(multipliers:options:modulus:modulooffset:).md)
### Configuring deformation
- [var multipliers: _Proto_LowLevelDeformationDescription_v1.Buffer](canarydescription/multipliers.md)
- [var options: _Proto_LowLevelDeformationDescription_v1.SemanticOptions](canarydescription/options.md)
- [var modulus: Int](canarydescription/modulus.md)
- [var moduloOffset: Int](canarydescription/modulooffset.md)
- [var sparse: Bool](canarydescription/sparse.md)
### Querying semantic options
- [func deforms() -> _Proto_LowLevelDeformationDescription_v1.SemanticOptions](canarydescription/deforms.md)
- [func requires() -> _Proto_LowLevelDeformationDescription_v1.SemanticOptions](canarydescription/requires.md)
### Identifying the description
- [func name() -> String](canarydescription/name.md)

## See Also

- [class LowLevelDeformation](lowleveldeformation.md)
  An object that encodes blend-shape, skinning, and renormalization passes into a Metal compute command encoder.
- [class LowLevelDeformationContext](lowleveldeformationcontext.md)
  An object that manages shared resources for [`LowLevelDeformation`](lowleveldeformation.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/canarydescription)*