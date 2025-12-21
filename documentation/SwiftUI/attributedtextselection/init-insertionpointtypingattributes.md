# init(insertionPoint:typingAttributes:)

**Framework**: SwiftUI  
**Kind**: init

Initialize a selection to a single insertion point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(insertionPoint: AttributedString.Index, typingAttributes: AttributeContainer? = nil)
```

## Parameters

- `insertionPoint`: The index of the string where the   charet should be positioned.
- `typingAttributes`: The attributes for the next character   that is typed, or   if they should be inferred from the attributes   on the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/init(insertionpoint:typingattributes:))*