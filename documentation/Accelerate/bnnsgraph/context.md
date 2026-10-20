# BNNSGraph.Context

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A wrapper around a compiled graph object that adds a required modifiable context to support dynamically sized models and set execute-time options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS
- watchOS 11.0+

## Declaration

```swift
class Context
```

#### Overview

A [`BNNSGraph.Context`](./context.md) instance provides a wrapper around the C API [`bnns_graph_t`](../bnns_graph_t.md) and [`bnns_graph_context_t`](../bnns_graph_context_t.md) types. Because this class manages its own memory, you don’t need to call [`BNNSGraphContextDestroy(_:)`](../bnnsgraphcontextdestroy%28_%29.md) to deallocate its resources.

## Topics

### Creating a graph context
- [BNNSGraph.CompileOptions](./compileoptions.md)
  The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.
### Specifying and querying a graph context’s properties
- [func setDynamicShapes([BNNSGraph.Shape], forFunction: String?) async throws -> [BNNSGraph.Shape]](./context/setdynamicshapes%28_,forfunction%29.md)
  Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.
- [BNNSGraph.Shape](./shape.md)
  The specification of the shape of an argument.
- [func argumentCount(forFunction: String?) -> Int](./context/argumentcount%28forfunction%29.md)
  Returns the number of arguments for the given function argument.
- [func argumentNames(forFunction: String?) -> [String]](./context/argumentnames%28forfunction%29.md)
  Returns the names of arguments for the given function argument.
- [func argumentPosition(forFunction: String?, argument: String) -> Int](./context/argumentposition%28forfunction,argument%29.md)
  Returns the index into the arguments array for the given function argument.
- [var functionCount: Int](./context/functioncount.md)
  The number of input arguments for the given function argument.
- [var functionNames: [String]](./context/functionnames.md)
  Returns the names of callable functions in the graph.
- [var checkForNaNsAndInfinities: Bool](./context/checkfornansandinfinities.md)
  A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.
### Specifying a tensor’s properties
- [func tensor(forFunction: String?, argument: String, fillKnownDynamicShapes: Bool) -> BNNSTensor?](./context/tensor%28forfunction,argument,fillknowndynamicshapes%29.md)
  Returns an unallocated tensor for a given function argument.
### Executing a graph
- [func executeFunction(String?, arguments: inout [BNNSTensor]) async throws](./context/executefunction%28_,arguments%29-8bhcn.md)
  Executes the specified function using an array of input and output tensors.
- [func executeFunction<T>(String?, arguments: [T]) throws](./context/executefunction%28_,arguments%29-95snr.md)
  Executes the specified function using an array of input and output pointers.
- [BNNSGraph.PointerArgument](./pointerargument.md)
  A type that BNNS Graph accepts as an input-output argument.
### Handling errors
- [BNNSGraph.Error](./error.md)
  Error codes that a graph context throws.
### Initializers
- [init(compileFromPath: String, functionName: String?, options: BNNSGraph.CompileOptions) async throws](./context/init%28compilefrompath,functionname,options%29-3nn5g.md)
  Returns a new context that wraps a graph object which represents the compiled `.mlmodelc` file.
- [init(compileFromPath: String, functionName: String?, options: BNNSGraph.CompileOptions) throws](./context/init%28compilefrompath,functionname,options%29-6ghot.md)
  Synchronously returns a new context that wraps a graph object which represents the compiled `.mlmodelc` file.
### Instance Properties
- [var streamingAdvanceCount: Int](./context/streamingadvancecount.md)
  Sets streaming advancement amount for cases with dynamically shaped inputs.
### Instance Methods
- [func allocateTensor(forFunction: String?, argument: String, fillKnownDynamicShapes: Bool) -> BNNSTensor?](./context/allocatetensor%28forfunction,argument,fillknowndynamicshapes%29.md)
  Returns an allocated tensor for a given function argument.
- [func executeFunction(String?, arguments: inout [BNNSTensor]) throws](./context/executefunction%28_,arguments%29-52eh3.md)
  Synchronously executes the specified function with the provided context.
- [func setBatchSize(Int, forFunction: String?) async](./context/setbatchsize%28_,forfunction%29-4872x.md)
  Sets the batch size for a graph.
- [func setBatchSize(Int, forFunction: String?)](./context/setbatchsize%28_,forfunction%29-8eqzm.md)
  Synchronously sets the batch size for a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context)*