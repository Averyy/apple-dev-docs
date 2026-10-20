# makeDynamicLibrary(library:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new dynamic library from a library containing Metal IR code synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary
```

```objc
- (id<MTLDynamicLibrary>) newDynamicLibrary:(id<MTLLibrary>) library error:(NSError **) error;
```

#### Return Value

A new dynamic Metal library upon success, `nil` otherwise.

## Parameters

- `library`: A library from which this compiler creates the new a dynamic library

## Default Implementations

### MTL4Compiler Implementations
- [func makeDynamicLibrary(library: any MTLLibrary) async throws -> any MTLDynamicLibrary](./makedynamiclibrary%28library%29-7f4yz.md)
  Creates a dynamic library asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(library:))*