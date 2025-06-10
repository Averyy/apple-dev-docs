# append(referenceOf:optimizeDepth:)

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
mutating func append(referenceOf other: CMReadOnlyDataBlockBuffer, optimizeDepth: Bool = true)
```

#### Discussion

The range within the block buffer is not required to be contiguous. Providing out of bounds range will result in a precondition failure.

## Parameters

- `optimizeDepth`: Keep the depth of buffer reference graph to a minimum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/append(referenceof:optimizedepth:)-2x1ta)*