# com.apple.developer.journal.allow

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that enables an app to present the journaling suggestions picker.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Details

- **Name**: `com.apple.developer.journal.allow`
- **Type**: array of string 

## Possible Values

- `suggestions`

#### Discussion

The [Journaling Suggestions](../../JournalingSuggestions/JournalingSuggestions.md) framework can’t present the [`JournalingSuggestionsPicker`](../../JournalingSuggestions/journalingsuggestionspicker.md) for apps without this entitlement in their code signature. Add this entitlement to your app by enabling the Journaling Suggestions capability in Xcode.

![Screenshot of the Capabilities pane in Xcode with the Journaling Suggestions capability selected.](https://developer.apple.com/tutorials/images/com.apple.bundleresources/media-4309269@2x.png)

For more information about presenting journaling suggestions in your app, see [Presenting the suggestions picker and processing a selection](../../JournalingSuggestions/presenting-the-suggestions-picker-and-processing-a-selection.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.journal.allow)*