# System and in-app search

**Framework**: App Intents

Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.

#### Overview

The `.system` domain defines app schemas that provide a structured representation for common search actions and content. Apply schemas in the `.system` domain to make your app’s search and content access available to Apple Intelligence and Siri.

Unlike other domains that target a specific app category, the `.system` domain applies broadly. Any app that enables searching or opening content can adopt these schemas.

- **[`search`](appschema/systemintent/search.md)**: An intent that searches in your app when people say phrases like “Find bicycle.” or “Search for mountains.”
- **[`open`](appschema/systemintent/open.md)**: An intent that opens content in your app when people say phrases like “Open my screenshot.png file.”

> 💡 **Tip**: Xcode generates a template implementation when you type `system_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Actions
- [var open: some AppSchemaIntent](appschema/systemintent/open.md)
  An intent schema that opens an item in the application.
- [var search: some AppSchemaIntent](appschema/systemintent/search.md)
  An intent schema that navigates to search results.
- [AppSchema.SystemIntent](appschema/systemintent.md)
  Identifies intent schemas in the system domain.

## See Also

- [Audio](app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Calendar](app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Camera](app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
- [Clock](app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Files](app-schema-domain-files.md)
  Make your file-management app’s actions available to Apple Intelligence and Siri by adopting schemas for common file actions.
- [Mail](app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Notes](app-schema-domain-notes.md)
  Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.
- [Phone](app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Photos](app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-system-and-in-app-search)*