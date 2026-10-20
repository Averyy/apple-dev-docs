# makeLibrary(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new Metal library synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeLibrary(descriptor: MTL4LibraryDescriptor) throws -> any MTLLibrary
```

```objc
- (id<MTLLibrary>) newLibraryWithDescriptor:(MTL4LibraryDescriptor *) descriptor error:(NSError **) error;
```

#### Return Value

A Metal library instance upon success, `nil` otherwise.

## Parameters

- `descriptor`: A description of the library to create.

## Default Implementations

### MTL4Compiler Implementations
- [func makeLibrary(descriptor: MTL4LibraryDescriptor) async throws -> any MTLLibrary](./makelibrary%28descriptor%29-6c46o.md)
  Creates a new Metal library asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makelibrary(descriptor:))*