# makeLibrary(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new Metal library asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeLibrary(descriptor: MTL4LibraryDescriptor) async throws -> any MTLLibrary
```

## Return Value

A Metal library instance upon success, otherwise this function throws.

## Parameters

- `descriptor`: A description of the library to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makelibrary(descriptor:)-6c46o)*