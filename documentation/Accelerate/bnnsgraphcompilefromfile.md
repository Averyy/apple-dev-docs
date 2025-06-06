# BNNSGraphCompileFromFile(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Compiles a source mlmodelc file to a graph object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func BNNSGraphCompileFromFile(_ filename: UnsafePointer<CChar>, _ function: UnsafePointer<CChar>?, _ options: bnns_graph_compile_options_t) -> bnns_graph_t
```

#### Return Value

A compiled graph object. If the operation fails, the graph object’s [`data`](bnns_graph_t/data.md) property is `nil`.

#### Discussion

Xcode automatically compiles a Core ML model package (files with an `.mlpackage` file extension) into an mlmodelc file. The following code compiles a [`bnns_graph_t`](bnns_graph_t.md) instance from a file named `myModel.mlpackage` that you copy into the project.

```swift
let options = BNNSGraphCompileOptionsMakeDefault()
defer {
    BNNSGraphCompileOptionsDestroy(options)
}

guard let fileName = Bundle.main.url(
    forResource: "myModel",
    withExtension: "mlmodelc")?.path() else {
    fatalError()
}

let graph = BNNSGraphCompileFromFile(fileName, 
                                     nil,
                                     options)

if graph.size == 0 {
    fatalError()
}
```

## Parameters

- `filename`: The path to the source mlmodelc file.
- `function`: The name of the function that this operation compiles. Pass   to specify that the operation compiles all the functions in the source file.
- `options`: The compilation options. Pass   to specify that the operation uses the default set of options.

## See Also

- [Updating a Model File to a Model Package](../CoreML/updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [struct bnns_graph_t](bnns_graph_t.md)
  The compiled graph object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcompilefromfile(_:_:_:))*