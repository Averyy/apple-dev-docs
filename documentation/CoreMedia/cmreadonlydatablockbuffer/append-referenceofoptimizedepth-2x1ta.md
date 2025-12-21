# append(referenceOf:optimizeDepth:)

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
mutating func append(referenceOf other: CMReadOnlyDataBlockBuffer, optimizeDepth: Bool = true)
```

#### Discussion

The range within the block buffer is not required to be contiguous. Providing out of bounds range will result in a precondition failure.

## Parameters

- `optimizeDepth`: Keep the depth of buffer reference graph to a minimum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/append(referenceof:optimizedepth:)-2x1ta)*