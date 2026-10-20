# storeFunctionInMetalScript

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that instructs the compiler to store function information for inspecting binary archives.

**Availability**:
- iOS 17.0+ - Deprecated in 18.0 (renamed: MTLFunctionOptions.storeFunctionInMetalPipelinesScript)
- iPadOS 17.0+ - Deprecated in 18.0 (renamed: MTLFunctionOptions.storeFunctionInMetalPipelinesScript)
- Mac Catalyst 17.0+ - Deprecated in 18.0 (renamed: MTLFunctionOptions.storeFunctionInMetalPipelinesScript)
- macOS 14.0+ - Deprecated in 15.0 (renamed: MTLFunctionOptions.storeFunctionInMetalPipelinesScript)
- tvOS 17.0+ - Deprecated in 18.0 (renamed: MTLFunctionOptions.storeFunctionInMetalPipelinesScript)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: MTLFunctionOptions.storeFunctionInMetalPipelinesScript)

> **Deprecated**: Use [`storeFunctionInMetalPipelinesScript`](./storefunctioninmetalpipelinesscript.md) instead.

## Declaration

```swift
static var storeFunctionInMetalScript: MTLFunctionOptions { get }
```

```c
MTLFunctionOptionStoreFunctionInMetalScript
```

## See Also

### Function compilation options
- [static var failOnBinaryArchiveMiss: MTLFunctionOptions](./failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var compileToBinary: MTLFunctionOptions](./compiletobinary.md)
  An option that instructs the compiler to generate a binary format for dynamic linking.
- [static var pipelineIndependent: MTLFunctionOptions](./pipelineindependent.md)
  An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions](./storefunctioninmetalpipelinesscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions/storefunctioninmetalscript)*