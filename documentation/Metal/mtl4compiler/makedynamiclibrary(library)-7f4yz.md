# makeDynamicLibrary(library:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a dynamic library asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeDynamicLibrary(library: any MTLLibrary) async throws -> any MTLDynamicLibrary
```

## Return Value

A dynamic library upon success, otherwise this method throws.

## Parameters

- `library`: A library the compiler uses to create a dynamic library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(library:)-7f4yz)*