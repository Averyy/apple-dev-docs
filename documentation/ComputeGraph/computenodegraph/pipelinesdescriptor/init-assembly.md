# init(assembly:)

**Framework**: Compute Graph  
**Kind**: init

Creates a descriptor configured for the given graph assembly.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
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