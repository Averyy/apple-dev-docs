# privacy

**Framework**: SwiftUI  
**Kind**: property

Displayed data should be obscured to protect private information.

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
static let privacy: RedactionReasons
```

#### Discussion

Views marked with `privacySensitive` will be automatically redacted using a standard styling. To apply a custom treatment the redaction reason can be read out of the environment.

```swift
struct BankingContentView: View {
    @Environment(\.redactionReasons) var redactionReasons

    var body: some View {
        if redactionReasons.contains(.privacy) {
            FullAppCover()
        } else {
            AppContent()
        }
    }
}
```

## See Also

- [static let invalidated: RedactionReasons](redactionreasons/invalidated.md)
  Displayed data should appear as invalidated and pending a new update.
- [static let placeholder: RedactionReasons](redactionreasons/placeholder.md)
  Displayed data should appear as generic placeholders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/redactionreasons/privacy)*