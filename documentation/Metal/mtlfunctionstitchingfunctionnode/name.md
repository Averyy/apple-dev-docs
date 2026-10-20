# name

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The name of the function to call.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

```objc
@property (nonatomic, copy, readwrite, nonnull) NSString * name;
```

#### Discussion

The name needs to match one of the functions in the stitched library descriptor’s [`functions`](../mtlstitchedlibrarydescriptor/functions.md) property.

## See Also

### Configuring a function node
- [var arguments: [any MTLFunctionStitchingNode]](./arguments.md)
  An ordered list of the nodes that provide the function’s arguments.
- [var controlDependencies: [MTLFunctionStitchingFunctionNode]](./controldependencies.md)
  The list of nodes that need to execute before executing the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/name)*