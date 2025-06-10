# typingAttributes(in:)

**Framework**: SwiftUI  
**Kind**: method

Returns the typing attributes for a corresponding text.

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
func typingAttributes(in text: AttributedString) -> AttributeContainer
```

#### Discussion

The typing attributes are the attributes that will be applied to any new characters typed out by the user.

> **Note**: The returned container may contain values for attributes that specify `runBoundaries` and thus might not actually get applied to new content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/typingattributes(in:))*