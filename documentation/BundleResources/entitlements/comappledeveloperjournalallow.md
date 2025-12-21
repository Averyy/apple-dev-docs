# com.apple.developer.journal.allow

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that enables an app to present the journaling suggestions picker.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

#### Discussion

The [`Journaling Suggestions`](https://developer.apple.com/documentation/JournalingSuggestions) framework can’t present the [`JournalingSuggestionsPicker`](https://developer.apple.com/documentation/JournalingSuggestions/JournalingSuggestionsPicker) for apps without this entitlement in their code signature. Add this entitlement to your app by enabling the Journaling Suggestions capability in Xcode.

![Screenshot of the Capabilities pane in Xcode with the Journaling Suggestions capability selected.](https://docs-assets.developer.apple.com/published/a4c58553c13202d4fc9603d740ccf2d7/media-4309269%402x.png)

For more information about presenting journaling suggestions in your app, see [`Presenting the suggestions picker and processing a selection`](https://developer.apple.com/documentation/JournalingSuggestions/presenting-the-suggestions-picker-and-processing-a-selection).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.journal.allow)*