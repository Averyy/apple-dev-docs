# init(transformComponent:resetsTransform:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(transformComponent component: any MDLTransformComponent, resetsTransform: Bool)
```

```objc
- (instancetype) initWithTransformComponent:(id<MDLTransformComponent>) component resetsTransform:(BOOL) resetsTransform;
```

## See Also

### Creating a Transform Object
- [convenience init(identity: ())](./init%28identity%29.md)
  Initializes a transform object to the identity transformation.
- [convenience init(matrix: matrix_float4x4)](./init%28matrix%29.md)
  Initializes a transform object with the specified transform matrix.
- [convenience init(transformComponent: any MDLTransformComponent)](./init%28transformcomponent%29.md)
  Initializes a transform object to match the specified transform component.
- [convenience init(matrix: matrix_float4x4, resetsTransform: Bool)](./init%28matrix,resetstransform%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/init(transformcomponent:resetstransform:))*