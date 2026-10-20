# vertexAttributes

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array that describes the vertex input attributes to a vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var vertexAttributes: [MTLVertexAttribute]? { get }
```

```objc
@property (readonly, nullable) NSArray<MTLVertexAttribute *> * vertexAttributes;
```

## See Also

### Retrieving function attributes
- [var stageInputAttributes: [MTLAttribute]?](./stageinputattributes.md)
  An array that describes the input attributes to the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/vertexattributes)*