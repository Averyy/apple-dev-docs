# init(assembly:)

**Framework**: Compute Graph  
**Kind**: init

Creates a descriptor configured for the given graph assembly.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
init(assembly: ComputeNodeGraph.Assembly)
```

#### Discussion

`options` defaults to [`init()`](computenodegraph/pipelines/options-swift.struct/init().md) and `libraries` is empty. Add shader libraries with [`addLibrary(_:bundle:)`](computenodegraph/pipelinesdescriptor/addlibrary(_:bundle:).md) before compiling.

## Parameters

- `assembly`: The assembled compute graph to compile pipelines for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/pipelinesdescriptor/init(assembly:))*