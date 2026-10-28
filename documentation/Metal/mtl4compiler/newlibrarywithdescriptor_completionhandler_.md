# newLibraryWithDescriptor:completionHandler:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new Metal library instance asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4CompilerTask>) newLibraryWithDescriptor:(MTL4LibraryDescriptor *) descriptor completionHandler:(MTLNewLibraryCompletionHandler) completionHandler;
```

## Return Value

A compiler task representing the asynchronous compilation task.

## Parameters

- `descriptor`: A description of the library to create.
- `completionHandler`: A block Metal calls when it finishes the build task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newlibrarywithdescriptor:completionhandler:)*