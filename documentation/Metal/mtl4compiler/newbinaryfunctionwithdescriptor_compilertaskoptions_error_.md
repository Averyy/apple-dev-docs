# newBinaryFunctionWithDescriptor:compilerTaskOptions:error:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new binary visible or intersection function synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4BinaryFunction>) newBinaryFunctionWithDescriptor:(MTL4BinaryFunctionDescriptor *) descriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions error:(NSError **) error;
```

#### Return Value

A new binary function upon success, `nil` otherwise.

## Parameters

- `descriptor`: A binary function descriptor to use for creating the binary function.
- `compilerTaskOptions`: A descriptor of the compilation itself, providing parameters that influence execution of the compilation process.
- `error`: An optional parameter into which Metal stores information in case of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor:compilertaskoptions:error:)*