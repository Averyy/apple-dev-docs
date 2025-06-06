# placeholder

**Framework**: SwiftUI  
**Kind**: property

Displayed data should appear as generic placeholders.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let placeholder: RedactionReasons
```

#### Discussion

Text and images will be automatically masked to appear as generic placeholders, though maintaining their original size and shape. Use this to create a placeholder UI without directly exposing placeholder data to users.

## See Also

- [static let invalidated: RedactionReasons](redactionreasons/invalidated.md)
  Displayed data should appear as invalidated and pending a new update.
- [static let privacy: RedactionReasons](redactionreasons/privacy.md)
  Displayed data should be obscured to protect private information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/redactionreasons/placeholder)*