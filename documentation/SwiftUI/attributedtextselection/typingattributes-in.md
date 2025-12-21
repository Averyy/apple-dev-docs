# typingAttributes(in:)

**Framework**: SwiftUI  
**Kind**: method

Returns the typing attributes for a corresponding text.

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
func typingAttributes(in text: AttributedString) -> AttributeContainer
```

#### Discussion

The typing attributes are the attributes that will be applied to any new characters typed out by the user.

> **Note**: The returned container may contain values for attributes that specify [`runBoundaries`](https://developer.apple.com/documentation/Foundation/AttributedStringKey/runBoundaries) and thus might not actually get applied to new content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/typingattributes(in:))*