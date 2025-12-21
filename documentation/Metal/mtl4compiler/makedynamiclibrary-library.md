# makeDynamicLibrary(library:)

**Framework**: Metal  
**Kind**: method  
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

#### Return Value

A new dynamic Metal library upon success, `nil` otherwise.

## Parameters

- `library`: A library from which this compiler creates the new a dynamic library


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(library:))*