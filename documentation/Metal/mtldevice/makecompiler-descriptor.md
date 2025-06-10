# makeCompiler(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new compiler from a compiler descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeCompiler(descriptor: MTL4CompilerDescriptor) throws -> any MTL4Compiler
```

#### Return Value

A [`MTL4Compiler`](mtl4compiler.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A   instance that configures the    instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecompiler(descriptor:))*