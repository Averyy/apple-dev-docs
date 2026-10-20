# MDLTransformStack

**Framework**: Model I/O  
**Kind**: class  
**Role**: Class

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

```objc
@interface MDLTransformStack : NSObject
```

## Topics

### Initializers
- [init()](./mdltransformstack/init%28%29.md)
### Instance Properties
- [var keyTimes: [NSNumber]](./mdltransformstack/keytimes.md)
- [var transformOps: [any MDLTransformOp]](./mdltransformstack/transformops.md)
### Instance Methods
- [func addMatrixOp(String, inverse: Bool) -> MDLTransformMatrixOp](./mdltransformstack/addmatrixop%28_,inverse%29.md)
- [func addOrientOp(String, inverse: Bool) -> MDLTransformOrientOp](./mdltransformstack/addorientop%28_,inverse%29.md)
- [func addRotateOp(String, order: MDLTransformOpRotationOrder, inverse: Bool) -> MDLTransformRotateOp](./mdltransformstack/addrotateop%28_,order,inverse%29.md)
- [func addRotateXOp(String, inverse: Bool) -> MDLTransformRotateXOp](./mdltransformstack/addrotatexop%28_,inverse%29.md)
- [func addRotateYOp(String, inverse: Bool) -> MDLTransformRotateYOp](./mdltransformstack/addrotateyop%28_,inverse%29.md)
- [func addRotateZOp(String, inverse: Bool) -> MDLTransformRotateZOp](./mdltransformstack/addrotatezop%28_,inverse%29.md)
- [func addScaleOp(String, inverse: Bool) -> MDLTransformScaleOp](./mdltransformstack/addscaleop%28_,inverse%29.md)
- [func addTranslateOp(String, inverse: Bool) -> MDLTransformTranslateOp](./mdltransformstack/addtranslateop%28_,inverse%29.md)
- [func animatedValue(withName: String) -> MDLAnimatedValue](./mdltransformstack/animatedvalue%28withname%29.md)
- [func count() -> Int](./mdltransformstack/count%28%29.md)
- [func double4x4(atTime: TimeInterval) -> matrix_double4x4](./mdltransformstack/double4x4%28attime%29.md)
- [func float4x4(atTime: TimeInterval) -> matrix_float4x4](./mdltransformstack/float4x4%28attime%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MDLComponent](./mdlcomponent.md)
- [MDLTransformComponent](./mdltransformcomponent.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformstack)*