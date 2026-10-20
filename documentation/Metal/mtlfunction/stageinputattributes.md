# stageInputAttributes

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array that describes the input attributes to the function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var stageInputAttributes: [MTLAttribute]? { get }
```

```objc
@property (readonly, nullable) NSArray<MTLAttribute *> * stageInputAttributes;
```

## See Also

### Retrieving function attributes
- [var vertexAttributes: [MTLVertexAttribute]?](./vertexattributes.md)
  An array that describes the vertex input attributes to a vertex function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/stageinputattributes)*