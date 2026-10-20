# tileArguments

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS 11.0+ - Deprecated in 13.0
- tvOS 14.5+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`tileBindings`](./tilebindings.md) instead.

## Declaration

```swift
var tileArguments: [MTLArgument]? { get }
```

```objc
@property (readonly, nullable) NSArray<MTLArgument *> * tileArguments;
```

#### Discussion

The [`MTLArgument`](../mtlargument.md) elements in the array are in the same order as the tile shader’s declaration signature.

## See Also

### Deprecated
- [var vertexArguments: [MTLArgument]?](./vertexarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader.
- [var fragmentArguments: [MTLArgument]?](./fragmentarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/tilearguments)*