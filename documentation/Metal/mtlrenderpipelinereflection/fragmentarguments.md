# fragmentArguments

**Framework**: Metal  
**Kind**: property

An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var fragmentArguments: [MTLArgument]? { get }
```

#### Discussion

The [`MTLArgument`](mtlargument.md) elements in the array are in the same order as the fragment shader’s declaration signature.

## See Also

- [var vertexArguments: [MTLArgument]?](mtlrenderpipelinereflection/vertexarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader.
- [var tileArguments: [MTLArgument]?](mtlrenderpipelinereflection/tilearguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/fragmentarguments)*