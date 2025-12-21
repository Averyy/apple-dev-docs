# arguments

**Framework**: Metal  
**Kind**: property

An array of instances that describe the arguments of a compute function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var arguments: [MTLArgument] { get }
```

#### Discussion

Each element in the array is an [`MTLArgument`](mtlargument.md) instance that describes one of the function’s arguments. The elements in the array are in the same order that the arguments appear in the function declaration.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection/arguments)*