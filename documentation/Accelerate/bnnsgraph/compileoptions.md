# BNNSGraph.CompileOptions

**Framework**: Accelerate  
**Kind**: struct

The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.

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
struct CompileOptions
```

#### Overview

Call `/Accelerate/BNNSGraph/Context/init(compileFromPath:functionName:options:)` to create a default options structure and then set properties such as [`optimizationPreference`](bnnsgraph/compileoptions/optimizationpreference-swift.property.md) to specify individual options.

## Topics

### Creating a compilation options structure
- [init()](bnnsgraph/compileoptions/init.md)
  Creates an allocated compilation-options object with default values.
- [init(useSingleThread: Bool, generateDebugInfo: Bool, optimizationPreference: BNNSGraph.CompileOptions.OptimizationPreference)](bnnsgraph/compileoptions/init(usesinglethread:generatedebuginfo:optimizationpreference:).md)
  Creates an allocated compilation-options object with the specified values.
### Specifying and querying compilation options
- [var useSingleThread: Bool](bnnsgraph/compileoptions/usesinglethread.md)
  A Boolean value that specifies whether the graph executes on one thread.
- [var generateDebugInfo: Bool](bnnsgraph/compileoptions/generatedebuginfo.md)
  A Boolean value that specifies whether the generated graph includes debug info.
- [var optimizationPreference: BNNSGraph.CompileOptions.OptimizationPreference](bnnsgraph/compileoptions/optimizationpreference-swift.property.md)
  A constant that specifies the graph compilation-optimization preferences.
### Specifying the optimization preference
- [BNNSGraph.CompileOptions.OptimizationPreference](bnnsgraph/compileoptions/optimizationpreference-swift.struct.md)
  Constants that describe the compilation-optimization preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/compileoptions)*