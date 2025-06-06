# NSTextWritingDirectionOverride

**Framework**: AppKit  
**Kind**: var

**Availability**:
- macOS 10.0+

## Declaration

```swift
var NSTextWritingDirectionOverride: Int { get }
```

#### Discussion

Enables character types with inherent directionality to be overridden when required for special cases, such as for part numbers made of mixed English, digits, and Hebrew letters to be written from right to left.

Use the [`NSWritingDirectionFormatType.override`](nswritingdirectionformattype/override.md) constant instead.

## See Also

- [var NSTextWritingDirectionEmbedding: Int](nstextwritingdirectionembedding.md)
  Text is embedded in text with another writing direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextwritingdirectionoverride)*