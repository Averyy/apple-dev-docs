# makeBinaryFunction(descriptor:compilerTaskOptions:)

**Framework**: Metal  
**Kind**: method

Creates a new binary visible or intersection function synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) throws -> any MTL4BinaryFunction
```

#### Return Value

A binary function upon success, otherwise this function throws.

## Parameters

- `descriptor`: A binary function descriptor to use for creating the binary function.
- `compilerTaskOptions`: A descriptor of the compilation itself, providing parameters that   influence execution of the compilation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makebinaryfunction(descriptor:compilertaskoptions:)-5o46e)*