# newBinaryFunctionWithDescriptor:compilerTaskOptions:completionHandler:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Returns a new compiler task that asyncrhonously creates a binary version of a GPU visible function or GPU intersection function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4CompilerTask>) newBinaryFunctionWithDescriptor:(MTL4BinaryFunctionDescriptor *) descriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions completionHandler:(MTL4NewBinaryFunctionCompletionHandler) completionHandler;
```

## Parameters

- `descriptor`: A configuration that tells the method which GPU function to make into a binary function and which options to apply when compiling it.
- `compilerTaskOptions`: A configuration for the compiler task.
- `completionHandler`: A completetion handler that you provide, which the task calls when it finishes compiling the binary function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newbinaryfunctionwithdescriptor:compilertaskoptions:completionhandler:)*