# makeDynamicLibrary(url:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new dynamic library from the contents of a file at an URL location synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary
```

#### Return Value

A new dynamic Metal library upon success, `nil` otherwise.

## Parameters

- `url`: An URL referencing a file whose contents this compiler uses to build a dynamic library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makedynamiclibrary(url:))*