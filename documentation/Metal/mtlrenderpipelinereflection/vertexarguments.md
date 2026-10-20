# vertexArguments

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`vertexBindings`](./vertexbindings.md) instead.

## Declaration

```swift
var vertexArguments: [MTLArgument]? { get }
```

```objc
@property (readonly, nullable) NSArray<MTLArgument *> * vertexArguments;
```

#### Discussion

The [`MTLArgument`](../mtlargument.md) elements in the array are in the same order as the vertex shader’s declaration signature.

## See Also

### Deprecated
- [var fragmentArguments: [MTLArgument]?](./fragmentarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader.
- [var tileArguments: [MTLArgument]?](./tilearguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/vertexarguments)*