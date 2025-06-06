# init(compileFromPath:functionName:options:)

**Framework**: Accelerate  
**Kind**: init

Returns a new context that wraps a graph object representing the compiled mlmodelc file.

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

## Parameters

- `path`: The path to the source mlmodelc file.
- `functionName`: The name of the function that this operation compiles. Pass   to specify that the operation compiles all the functions in the source file.
- `options`: The compilation options.

## See Also

- [func BNNSGraphCompileFromFile(UnsafePointer<CChar>, UnsafePointer<CChar>?, bnns_graph_compile_options_t) -> bnns_graph_t](bnnsgraphcompilefromfile(_:_:_:).md)
  Compiles a source mlmodelc file to a graph object.
- [func BNNSGraphContextMake(bnns_graph_t) -> bnns_graph_context_t](bnnsgraphcontextmake(_:).md)
  Returns an allocated and initialized graph context from the specified graph.
- [BNNSGraph.CompileOptions](bnnsgraph/compileoptions.md)
  The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/init(compilefrompath:functionname:options:))*