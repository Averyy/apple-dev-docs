# init(insertionPoint:typingAttributes:)

**Framework**: SwiftUI  
**Kind**: init

Initialize a selection to a single insertion point.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(insertionPoint: AttributedString.Index, typingAttributes: AttributeContainer? = nil)
```

## Parameters

- `insertionPoint`: The index of the string where the   charet should be positioned.
- `typingAttributes`: The attributes for the next character   that is typed, or   if they should be inferred from the attributes   on the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/init(insertionpoint:typingattributes:))*