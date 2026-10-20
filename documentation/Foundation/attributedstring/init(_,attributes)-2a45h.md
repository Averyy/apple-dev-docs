# init(_:attributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an attributed string from a string and an attribute container.

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
init(_ string: String, attributes: AttributeContainer = .init())
```

## Parameters

- `string`: A string to add attributes to.
- `attributes`: Attributes to apply to `string`.

## See Also

### Creating an Attributed String
- [init()](./init%28%29.md)
  Creates an empty attributed string.
- [init(AttributedSubstring)](./init%28_%29-8tnoq.md)
  Creates an attributed string from an attributed substring.
- [init(Substring, attributes: AttributeContainer)](./init%28_,attributes%29-8jqhp.md)
  Creates an attributed string from a substring and an attribute container.
- [init<S>(S, attributes: AttributeContainer)](./init%28_,attributes%29-8l0iq.md)
  Creates an attributed string from a character sequence and an attribute container.
- [struct AttributeContainer](../attributecontainer.md)
  A container for attribute keys and values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(_:attributes:)-2a45h)*