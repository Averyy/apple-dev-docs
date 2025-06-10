# makeLibrary(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new Metal library synchronously.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeLibrary(descriptor: MTL4LibraryDescriptor) throws -> any MTLLibrary
```

#### Return Value

A Metal library instance upon success, `nil` otherwise.

## Parameters

- `descriptor`: A description of the library to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makelibrary(descriptor:))*