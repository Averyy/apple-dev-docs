# formatSubstring

**Framework**: OSLog  
**Kind**: property

The text immediately preceding a placeholder.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var formatSubstring: String { get }
```

#### Discussion

The `formatSubstring` property can be an empty string if there is nothing between two placeholders, or if it is between the placeholder and the bounds of the string.

## See Also

- [var placeholder: String](oslogmessagecomponent/placeholder.md)
  The placeholder text for the message component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogmessagecomponent/formatsubstring)*