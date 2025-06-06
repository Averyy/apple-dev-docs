# init(_:attributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string from a character sequence and an attribute container.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init<S>(_ elements: S, attributes: AttributeContainer = .init()) where S : Sequence, S.Element == Character
```

## Parameters

- `elements`: A character sequence that provides the textual content for the attributed string.
- `attributes`: Attributes to apply to the textual content.

## See Also

- [init()](attributedstring/init.md)
  Creates an empty attributed string.
- [init(AttributedSubstring)](attributedstring/init(_:)-8tnoq.md)
  Creates an attributed string from an attributed substring.
- [init(String, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-2a45h.md)
  Creates an attributed string from a string and an attribute container.
- [init(Substring, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-8jqhp.md)
  Creates an attributed string from a substring and an attribute container.
- [struct AttributeContainer](attributecontainer.md)
  A container for attribute keys and values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(_:attributes:)-8l0iq)*