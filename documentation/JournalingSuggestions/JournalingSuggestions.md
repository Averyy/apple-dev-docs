# Journaling Suggestions

**Framework**: Journaling Suggestions  
**Kind**: module

Display a set of recent, personal events that inspire someone to contribute to your app’s creative workflow.

**Availability**:
- iOS 17.2+
- iPadOS 26.0+ (Beta)

#### Overview

Journaling Suggestions provides a visual picker interface for iPhone apps. The picker displays personal events that occur in someone’s life, such as a place they visited, a person they connected with, a photo in their library, or a song that they play repeatedly.

If your app facilitates personal writing, display the picker to provide people with ideas for their creative content. When someone chooses a suggestion from the picker, the system makes high-level details about the event available to your app. For example, a journaling app uses the details to display the beginning of a new journal entry about the selected suggestion.

![A figure that features two iPhone device frames in an app workflow progressing from left to right. The frame at left depicts several photos, including one of a flower, in a thumbnail view under text that reads Highlights from Photo Memories. A callout below reads Suggestions picker. The frame at right depicts a detailed version of the flower thumbnail below user-defined text that reads Coastal Hike.  Bars below the image represent a person’s writing above a callout that reads Journal entry.](https://docs-assets.developer.apple.com/published/530b2d27b0c6228b6f43b3f09e63e861/JournalingSuggestions%402x.png)

To incorporate a suggestions picker ([`JournalingSuggestionsPicker`](journalingsuggestionspicker.md)) in your app, declare it using [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI), and choose the text for a button that presents the picker.

For the picker to appear, your app needs a special entitlement in your app’s code signature. You don’t need to ask for additional authorization because your app can’t access the details for a suggestion until after a person chooses to share them by making a selection in the picker.

> **Note**: Mac apps built with Mac Catalyst ignore input if someone taps a suggestions picker button.

## Topics

### Essentials
- [Journaling Suggestions updates](../Updates/JournalingSuggestions.md)
  Learn about important changes in Journaling Suggestions.
- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)
  Display the journaling suggestions picker and process a suggestion that someone chooses.
- [com.apple.developer.journal.allow](../BundleResources/Entitlements/com.apple.developer.journal.allow.md)
  The entitlement that enables an app to present the journaling suggestions picker.
### Implementation
- [struct JournalingSuggestionsPicker](journalingsuggestionspicker.md)
  A view that lists different types of recent events in a person’s life.
- [struct JournalingSuggestion](journalingsuggestion.md)
  High-level information about a suggestion that a person chooses in the journaling suggestions picker.
- [class JournalingSuggestionsConfiguration](journalingsuggestionsconfiguration.md)
  The scheduled configuration settings for your app.
- [protocol JournalingSuggestionAsset](journalingsuggestionasset.md)
  An interface for the content that the suggestions picker presents.
- [struct JournalingSuggestionPresentationToken](journalingsuggestionpresentationtoken.md)
  A token you use to modify the content of the presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/JournalingSuggestions)*