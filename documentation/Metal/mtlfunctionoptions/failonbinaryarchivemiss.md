# failOnBinaryArchiveMiss

**Framework**: Metal  
**Kind**: property

An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static var failOnBinaryArchiveMiss: MTLFunctionOptions { get }
```

#### Discussion

By default, Metal compiles a function if it isn’t in a binary archive. When you set this option, Metal returns an error instead of compiling a missing function.

Setting this option is a way to verify that binary archives contain all the functions your app needs, or to measure a binary archive’s hit rates.

## See Also

- [static var compileToBinary: MTLFunctionOptions](mtlfunctionoptions/compiletobinary.md)
  An option that instructs the compiler to generate a binary format for dynamic linking.
- [static var pipelineIndependent: MTLFunctionOptions](mtlfunctionoptions/pipelineindependent.md)
  An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions](mtlfunctionoptions/storefunctioninmetalpipelinesscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [static var storeFunctionInMetalScript: MTLFunctionOptions](mtlfunctionoptions/storefunctioninmetalscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions/failonbinaryarchivemiss)*