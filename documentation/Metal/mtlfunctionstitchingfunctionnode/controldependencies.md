# controlDependencies

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The list of nodes that need to execute before executing the node.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var controlDependencies: [MTLFunctionStitchingFunctionNode] { get set }
```

```objc
@property (nonatomic, copy, readwrite, nonnull) NSArray<MTLFunctionStitchingFunctionNode *> * controlDependencies;
```

#### Discussion

When a stitched function calls functions that have side effects on their input data, you often need the GPU to execute functions in a specific order. In such cases, use the [`controlDependencies`](./controldependencies.md) property to specify which nodes need to run before executing this node.

## See Also

### Configuring a function node
- [var name: String](./name.md)
  The name of the function to call.
- [var arguments: [any MTLFunctionStitchingNode]](./arguments.md)
  An ordered list of the nodes that provide the function’s arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/controldependencies)*