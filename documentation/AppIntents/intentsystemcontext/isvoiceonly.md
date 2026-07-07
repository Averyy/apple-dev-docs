# isVoiceOnly

**Framework**: App Intents  
**Kind**: property

A Boolean value that indicates whether the system performs the app intent in a voice-only context.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var isVoiceOnly: Bool { get }
```

#### Discussion

If [`isVoiceOnly`](intentsystemcontext/isvoiceonly.md) is `true`, adjust the intent’s result to include a more speakable summary, and make sure a person can understand responses and dialog without visuals such as tables, graphics, or other user-interface elements.

Generally, return an [`IntentDialog`](intentdialog.md) from your intent. The system can choose the best information from the dialog to present for a person’s context. Consult [`isVoiceOnly`](intentsystemcontext/isvoiceonly.md) when your app intent returns dynamic, free-form output, such as generated recommendations, summarized search results, or natural-language responses you generate on the fly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentsystemcontext/isvoiceonly)*