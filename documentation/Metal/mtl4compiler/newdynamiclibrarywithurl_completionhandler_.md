# newDynamicLibraryWithURL:completionHandler:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new dynamic library from the contents of a file at an URL location synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4CompilerTask>) newDynamicLibraryWithURL:(NSURL *) url completionHandler:(MTLNewDynamicLibraryCompletionHandler) completionHandler;
```

#### Return Value

A compiler task representing the asynchronous compilation task.

## Parameters

- `url`: An URL referencing a file whose contents this compiler uses to build a dynamic library.
- `completionHandler`: A block Metal calls when it finishes the build task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newdynamiclibrarywithurl:completionhandler:)*