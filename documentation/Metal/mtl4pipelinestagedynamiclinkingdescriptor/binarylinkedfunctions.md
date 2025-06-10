# binaryLinkedFunctions

**Framework**: Metal  
**Kind**: property

Provides the array of binary functions to link.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var binaryLinkedFunctions: [any MTL4BinaryFunction]? { get set }
```

#### Discussion

Binary functions are shader functions that you compile from Metal IR to machine code ahead of time using instances of [`MTL4Compiler`](mtl4compiler.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor/binarylinkedfunctions)*