# NSTextWritingDirectionOverride

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use NSWritingDirectionOverride instead

## Declaration

```swift
var NSTextWritingDirectionOverride: Int { get }
```

```c
NSTextWritingDirectionOverride
```

#### Discussion

Enables character types with inherent directionality to be overridden when required for special cases, such as for part numbers made of mixed English, digits, and Hebrew letters to be written from right to left.

Use the [`NSWritingDirectionFormatType.override`](./nswritingdirectionformattype/override.md) constant instead.

## See Also

### Constants
- [var NSTextWritingDirectionEmbedding: Int](./nstextwritingdirectionembedding.md)
  Text is embedded in text with another writing direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextwritingdirectionoverride)*