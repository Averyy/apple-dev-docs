# append(referenceOf:range:optimizeDepth:)

**Framework**: Core Media  
**Kind**: method

Append a reference to a range of another block buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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