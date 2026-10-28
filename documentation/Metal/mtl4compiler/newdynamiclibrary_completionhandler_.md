# newDynamicLibrary:completionHandler:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new dynamic Metal library instance asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4CompilerTask>) newDynamicLibrary:(id<MTLLibrary>) library completionHandler:(MTLNewDynamicLibraryCompletionHandler) completionHandler;
```

## Return Value

A compiler task representing the asynchronous compilation task.

## Parameters

- `library`: A library from which this compiler creates the new a dynamic library
- `completionHandler`: A block Metal calls when it finishes the build task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newdynamiclibrary:completionhandler:)*