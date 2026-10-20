# invalidated

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

Views marked with [`invalidatableContent(_:)`](../view/invalidatablecontent%28_%29.md) will be automatically redacted with a standard styling indicating the content is invalidated and new content will be available soon.

## See Also

### Getting redaction reasons
- [static let placeholder: RedactionReasons](./placeholder.md)
  Displayed data should appear as generic placeholders.
- [static let privacy: RedactionReasons](./privacy.md)
  Displayed data should be obscured to protect private information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/redactionreasons/invalidated)*