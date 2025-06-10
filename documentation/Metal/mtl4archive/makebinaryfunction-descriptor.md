# makeBinaryFunction(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Method used to create a binary function, with a given descriptor, from the contents of the archive.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor) throws -> any MTL4BinaryFunction
```

#### Return Value

A binary function object, otherwise `nil`.

## Parameters

- `descriptor`: The function descriptor for a visible or intersection function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4archive/makebinaryfunction(descriptor:))*