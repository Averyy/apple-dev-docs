# init(transformComponent:)

**Framework**: Model I/O  
**Kind**: init

Initializes a transform object to match the specified transform component.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(transformComponent component: any MDLTransformComponent)
```

#### Return Value

A new transform object.

#### Discussion

Use this method to copy transformation from any object that adopts the [`MDLTransformComponent`](mdltransformcomponent.md) protocol (such as another [`MDLTransform`](mdltransform.md) instance).

## Parameters

- `component`: The component whose transform information is to be copied.

## See Also

- [convenience init(identity: ())](mdltransform/init(identity:).md)
  Initializes a transform object to the identity transformation.
- [convenience init(matrix: matrix_float4x4)](mdltransform/init(matrix:).md)
  Initializes a transform object with the specified transform matrix.
- [convenience init(matrix: matrix_float4x4, resetsTransform: Bool)](mdltransform/init(matrix:resetstransform:).md)
- [convenience init(transformComponent: any MDLTransformComponent, resetsTransform: Bool)](mdltransform/init(transformcomponent:resetstransform:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/init(transformcomponent:))*