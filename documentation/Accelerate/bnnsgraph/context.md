# BNNSGraph.Context

**Framework**: Accelerate  
**Kind**: class

A wrapper around a compiled graph object that adds a required modifiable context to support dynamically sized models and set execute-time options.

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
class Context
```

#### Overview

A [`BNNSGraph.Context`](bnnsgraph/context.md) instance provides a wrapper around the C API [`bnns_graph_t`](bnns_graph_t.md) and [`bnns_graph_context_t`](bnns_graph_context_t.md) types. Because this class manages its own memory, you don’t need to call [`BNNSGraphContextDestroy(_:)`](bnnsgraphcontextdestroy(_:).md) to deallocate its resources.

## Topics

### Creating a graph context
- [init(compileFromPath: String, functionName: String?, options: BNNSGraph.CompileOptions) async throws](bnnsgraph/context/init(compilefrompath:functionname:options:).md)
  Returns a new context that wraps a graph object representing the compiled mlmodelc file.
- [BNNSGraph.CompileOptions](bnnsgraph/compileoptions.md)
  The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.
### Specifying and querying a graph context’s properties
- [func setBatchSize(Int, forFunction: String?) async](bnnsgraph/context/setbatchsize(_:forfunction:).md)
  Sets the batch size for a graph.
- [func setDynamicShapes([BNNSGraph.Shape], forFunction: String?) async throws -> [BNNSGraph.Shape]](bnnsgraph/context/setdynamicshapes(_:forfunction:).md)
  Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.
- [BNNSGraph.Shape](bnnsgraph/shape.md)
  The specification of the shape of an argument.
- [func argumentCount(forFunction: String?) -> Int](bnnsgraph/context/argumentcount(forfunction:).md)
  Returns the number of arguments for the given function argument.
- [func argumentNames(forFunction: String?) -> [String]](bnnsgraph/context/argumentnames(forfunction:).md)
  Returns the names of arguments for the given function argument.
- [func argumentPosition(forFunction: String?, argument: String) -> Int](bnnsgraph/context/argumentposition(forfunction:argument:).md)
  Returns the index into the arguments array for the given function argument.
- [var functionCount: Int](bnnsgraph/context/functioncount.md)
  The number of input arguments for the given function argument.
- [var functionNames: [String]](bnnsgraph/context/functionnames.md)
  Returns the names of callable functions in the graph.
- [var checkForNaNsAndInfinities: Bool](bnnsgraph/context/checkfornansandinfinities.md)
  A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.
### Specifying a tensor’s properties
- [func tensor(forFunction: String?, argument: String, fillKnownDynamicShapes: Bool) -> BNNSTensor?](bnnsgraph/context/tensor(forfunction:argument:fillknowndynamicshapes:).md)
  Returns an unallocated tensor for a given function argument.
### Executing a graph
- [func executeFunction(String?, arguments: inout [BNNSTensor]) async throws](bnnsgraph/context/executefunction(_:arguments:)-8bhcn.md)
  Executes the specified function using an array of input and output tensors.
- [func executeFunction<T>(String?, arguments: [T]) throws](bnnsgraph/context/executefunction(_:arguments:)-95snr.md)
  Executes the specified function using an array of input and output pointers.
- [BNNSGraph.PointerArgument](bnnsgraph/pointerargument.md)
  A type that BNNS Graph accepts as an input-output argument.
### Handling errors
- [BNNSGraph.Error](bnnsgraph/error.md)
  Error codes that a graph context throws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context)*