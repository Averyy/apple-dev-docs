# MDLTransformStack

**Framework**: Model I/O  
**Kind**: class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MDLTransformStack
```

## Topics

### Initializers
- [init()](mdltransformstack/init.md)
### Instance Properties
- [var keyTimes: [NSNumber]](mdltransformstack/keytimes.md)
- [var transformOps: [any MDLTransformOp]](mdltransformstack/transformops.md)
### Instance Methods
- [func addMatrixOp(String, inverse: Bool) -> MDLTransformMatrixOp](mdltransformstack/addmatrixop(_:inverse:).md)
- [func addOrientOp(String, inverse: Bool) -> MDLTransformOrientOp](mdltransformstack/addorientop(_:inverse:).md)
- [func addRotateOp(String, order: MDLTransformOpRotationOrder, inverse: Bool) -> MDLTransformRotateOp](mdltransformstack/addrotateop(_:order:inverse:).md)
- [func addRotateXOp(String, inverse: Bool) -> MDLTransformRotateXOp](mdltransformstack/addrotatexop(_:inverse:).md)
- [func addRotateYOp(String, inverse: Bool) -> MDLTransformRotateYOp](mdltransformstack/addrotateyop(_:inverse:).md)
- [func addRotateZOp(String, inverse: Bool) -> MDLTransformRotateZOp](mdltransformstack/addrotatezop(_:inverse:).md)
- [func addScaleOp(String, inverse: Bool) -> MDLTransformScaleOp](mdltransformstack/addscaleop(_:inverse:).md)
- [func addTranslateOp(String, inverse: Bool) -> MDLTransformTranslateOp](mdltransformstack/addtranslateop(_:inverse:).md)
- [func animatedValue(withName: String) -> MDLAnimatedValue](mdltransformstack/animatedvalue(withname:).md)
- [func count() -> Int](mdltransformstack/count.md)
- [func double4x4(atTime: TimeInterval) -> matrix_double4x4](mdltransformstack/double4x4(attime:).md)
- [func float4x4(atTime: TimeInterval) -> matrix_float4x4](mdltransformstack/float4x4(attime:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLComponent](mdlcomponent.md)
- [MDLTransformComponent](mdltransformcomponent.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformstack)*