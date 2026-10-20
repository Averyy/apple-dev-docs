# init(name:arguments:controlDependencies:)

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Creates a new function node.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(name: String, arguments: [any MTLFunctionStitchingNode], controlDependencies: [MTLFunctionStitchingFunctionNode])
```

```objc
- (instancetype) initWithName:(NSString *) name arguments:(NSArray<id<MTLFunctionStitchingNode>> *) arguments controlDependencies:(NSArray<MTLFunctionStitchingFunctionNode *> *) controlDependencies;
```

## Parameters

- `name`: The name of the function to call.
- `arguments`: An ordered list of the nodes that provide the function’s arguments.
- `controlDependencies`: The list of nodes that need to run before executing this node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/init(name:arguments:controldependencies:))*