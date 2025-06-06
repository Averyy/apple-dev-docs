# invalidated

**Framework**: SwiftUI  
**Kind**: property

Displayed data should appear as invalidated and pending a new update.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let invalidated: RedactionReasons
```

#### Discussion

Views marked with `invalidatableContent` will be automatically redacted with a standard styling indicating the content is invalidated and new content will be available soon.

## See Also

- [static let placeholder: RedactionReasons](redactionreasons/placeholder.md)
  Displayed data should appear as generic placeholders.
- [static let privacy: RedactionReasons](redactionreasons/privacy.md)
  Displayed data should be obscured to protect private information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/redactionreasons/invalidated)*