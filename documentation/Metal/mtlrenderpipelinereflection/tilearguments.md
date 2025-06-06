# tileArguments

**Framework**: Metal  
**Kind**: property

An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var tileArguments: [MTLArgument]? { get }
```

#### Discussion

The [`MTLArgument`](mtlargument.md) elements in the array are in the same order as the tile shader’s declaration signature.

## See Also

- [var vertexArguments: [MTLArgument]?](mtlrenderpipelinereflection/vertexarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader.
- [var fragmentArguments: [MTLArgument]?](mtlrenderpipelinereflection/fragmentarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/tilearguments)*