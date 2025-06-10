# makeDynamicLibrary(library:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new dynamic library from a library containing Metal IR code synchronously.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary
```

#### Return Value

A new dynamic Metal library upon success, `nil` otherwise.

## Parameters

- `library`: A library from which this compiler creates the new a dynamic library


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(library:))*