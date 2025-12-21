# binaryLinkedFunctions

**Framework**: Metal  
**Kind**: property

Provides the array of binary functions to link.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var binaryLinkedFunctions: [any MTL4BinaryFunction]? { get set }
```

#### Discussion

Binary functions are shader functions that you compile from Metal IR to machine code ahead of time using instances of [`MTL4Compiler`](mtl4compiler.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor/binarylinkedfunctions)*