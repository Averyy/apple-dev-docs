# pipelineIndependent

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var pipelineIndependent: MTLFunctionOptions { get }
```

```c
MTLFunctionOptionPipelineIndependent
```

#### Discussion

By default, when you link an [`MTLFunction`](../mtlfunction.md) into a pipeline state, Metal generates a function handle that points to that function’s location in the pipeline’s executable code. Because different pipeline states place functions at different memory addresses, Metal generates different function handles for the same function in each pipeline state. You insert function handles into an [`MTLIntersectionFunctionTable`](../mtlintersectionfunctiontable.md) or [`MTLVisibleFunctionTable`](../mtlvisiblefunctiontable.md) instance, which means you need separate function tables for each pipeline state by default.

When you compile a function with this option, Metal generates the same function handle for the function across all pipeline states that link it. This consistency lets you create a single function table and use it with multiple pipeline states, which reduces memory overhead and simplifies function table management.

> **Note**: This option only works with functions that you compile with the [`compileToBinary`](./compiletobinary.md) option.

## See Also

### Function compilation options
- [static var failOnBinaryArchiveMiss: MTLFunctionOptions](./failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var compileToBinary: MTLFunctionOptions](./compiletobinary.md)
  An option that instructs the compiler to generate a binary format for dynamic linking.
- [static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions](./storefunctioninmetalpipelinesscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [static var storeFunctionInMetalScript: MTLFunctionOptions](./storefunctioninmetalscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionNone](./mtlfunctionoptionnone.md)
  A sentinel value that represents an empty set of options, which is the default behavior for creating functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions/pipelineindependent)*