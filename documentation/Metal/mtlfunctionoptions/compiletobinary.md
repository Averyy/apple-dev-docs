# compileToBinary

**Framework**: Metal  
**Kind**: property

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

## See Also

- [static var failOnBinaryArchiveMiss: MTLFunctionOptions](mtlfunctionoptions/failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var pipelineIndependent: MTLFunctionOptions](mtlfunctionoptions/pipelineindependent.md)
  An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions](mtlfunctionoptions/storefunctioninmetalpipelinesscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [static var storeFunctionInMetalScript: MTLFunctionOptions](mtlfunctionoptions/storefunctioninmetalscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions/compiletobinary)*