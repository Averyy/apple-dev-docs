# init(compileFromPath:functionName:options:)

**Framework**: Accelerate  
**Kind**: init

Synchronously returns a new context that wraps a graph object which represents the compiled `.mlmodelc` file.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(compileFromPath path: String, functionName: String? = nil, options: BNNSGraph.CompileOptions = CompileOptions()) throws
```

#### Discussion

> **Note**: `BNNSGraphCompileFromFile`

> **Note**: `BNNSGraphContextMake`

## Parameters

- `path`: The path to the   program file.
- `functionName`: The name of a specific function to be compiled. Pass   to specify that the function compiles all functions.
- `options`: The compilation options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/init(compilefrompath:functionname:options:)-6ghot)*