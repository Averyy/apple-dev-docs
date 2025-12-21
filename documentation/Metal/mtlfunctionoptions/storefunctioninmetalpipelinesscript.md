# storeFunctionInMetalPipelinesScript

**Framework**: Metal  
**Kind**: property

An option that instructs the compiler to store function information for inspecting binary archives.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions { get }
```

#### Discussion

Set this option when you want to inspect or consume binary archives with the `metal-source` tool. You don’t need this option when you recompile functions or store them in binary archives.

## See Also

- [static var failOnBinaryArchiveMiss: MTLFunctionOptions](mtlfunctionoptions/failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var compileToBinary: MTLFunctionOptions](mtlfunctionoptions/compiletobinary.md)
  An option that instructs the compiler to generate a binary format for dynamic linking.
- [static var pipelineIndependent: MTLFunctionOptions](mtlfunctionoptions/pipelineindependent.md)
  An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [static var storeFunctionInMetalScript: MTLFunctionOptions](mtlfunctionoptions/storefunctioninmetalscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions/storefunctioninmetalpipelinesscript)*