# arguments

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An ordered list of the nodes that provide the function’s arguments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var arguments: [any MTLFunctionStitchingNode] { get set }
```

```objc
@property (nonatomic, copy, readwrite, nonnull) NSArray<id<MTLFunctionStitchingNode>> * arguments;
```

#### Discussion

Each node’s output data types needs to match the input data type of the matching argument.

## See Also

### Configuring a function node
- [var name: String](./name.md)
  The name of the function to call.
- [var controlDependencies: [MTLFunctionStitchingFunctionNode]](./controldependencies.md)
  The list of nodes that need to execute before executing the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/arguments)*