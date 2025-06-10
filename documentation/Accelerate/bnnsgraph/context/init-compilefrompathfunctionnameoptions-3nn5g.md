# init(compileFromPath:functionName:options:)

**Framework**: Accelerate  
**Kind**: init

Returns a new context that wraps a graph object which represents the compiled `.mlmodelc` file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
init(compileFromPath path: String, functionName: String? = nil, options: BNNSGraph.CompileOptions = CompileOptions()) async throws
```

#### Discussion

> **Note**: `BNNSGraphCompileFromFile`

> **Note**: `BNNSGraphContextMake`

## Parameters

- `path`: The path to the   program file.
- `functionName`: The name of a specific function to be compiled. Pass   to specify that the function compiles all functions.
- `options`: The compilation options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/init(compilefrompath:functionname:options:)-3nn5g)*