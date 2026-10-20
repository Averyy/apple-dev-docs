# init(assembly:)

**Framework**: Compute Graph  
**Kind**: init  
**Role**: Initializer

Creates a descriptor configured for the given graph assembly.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
init(assembly: ComputeNodeGraph.Assembly)
```

#### Discussion

`options` defaults to [`init()`](../pipelines/options-swift.struct/init%28%29.md) and `libraries` is empty. Add shader libraries with [`addLibrary(_:bundle:)`](./addlibrary%28_,bundle%29.md) before compiling.

## Parameters

- `assembly`: The assembled compute graph to compile pipelines for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/pipelinesdescriptor/init(assembly:))*