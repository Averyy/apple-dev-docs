# compileToBinary

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that instructs the compiler to generate a binary format for dynamic linking.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var compileToBinary: MTLFunctionOptions { get }
```

```c
MTLFunctionOptionCompileToBinary
```

## See Also

### Function compilation options
- [static var failOnBinaryArchiveMiss: MTLFunctionOptions](./failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var pipelineIndependent: MTLFunctionOptions](./pipelineindependent.md)
  An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions](./storefunctioninmetalpipelinesscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [static var storeFunctionInMetalScript: MTLFunctionOptions](./storefunctioninmetalscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionNone](./mtlfunctionoptionnone.md)
  A sentinel value that represents an empty set of options, which is the default behavior for creating functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions/compiletobinary)*