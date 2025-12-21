# append(referenceOf:range:optimizeDepth:)

**Framework**: Core Media  
**Kind**: method

Append a reference to a range of another block buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func append(referenceOf other: consuming CMMutableDataBlockBuffer, range: Range<Int>? = nil, optimizeDepth: Bool = true)
```

#### Discussion

The range within the block buffer is not required to be contiguous. Providing out of bounds range will result in a precondition failure.

## Parameters

- `range`: Range of bytes within the other block buffer to append. If  , the entire buffer is referenced.
- `optimizeDepth`: Keep the depth of buffer reference graph to a minimum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/append(referenceof:range:optimizedepth:))*