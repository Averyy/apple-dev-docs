# BEDirectionalTextRange

**Framework**: BrowserEngineKit  
**Kind**: struct

Modifications to text length based on its offset.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
struct BEDirectionalTextRange
```

#### Overview

This class encapsulates instructions that modify a text selection. In a given instance, the sign of [`length`](bedirectionaltextrange/length.md) determines the selection direction from its [`offset`](bedirectionaltextrange/offset.md). Positive length indicates moving the selection forward in the string, whereas a negative  [`length`](bedirectionaltextrange/length.md) moves the selection backward in the string. For example, applying a directional text range of `{ -6, -2 }` to the selection “world” in the string “Hello world” results in the selection, “Hel”.

## Topics

### Creating a directional text range
- [init()](bedirectionaltextrange/init.md)
  Creates an empty directional text range.
- [init(offset: Int, length: Int)](bedirectionaltextrange/init(offset:length:).md)
  Creates a range for a text selection that also specifies a direction.
### Measuring text range
- [var length: Int](bedirectionaltextrange/length.md)
  The number of characters included in the directional text range.
- [var offset: Int](bedirectionaltextrange/offset.md)
  The starting position of the directional text range within the text.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Sendable](../swift/sendable.md)

## See Also

- [protocol BEExtendedTextInputTraits](beextendedtextinputtraits.md)
  An object that customizes text-input appearance and behavior beyond the standard system traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedirectionaltextrange)*