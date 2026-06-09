# App schema domains

**Framework**: App Intents

Declare support for well-known actions and content by applying system-defined schemas to your app intents, app entities, and app enumerations.

#### Overview

Help the system correctly understand your app and its intents, entities, and enumerations by conforming your types to system-defined schemas whenever possible. Each schema tells the system how to interpret one of your app’s types. For example, when an email app conforms one of its intents to the `.mail.createDraft` schema, the system knows it can invoke that intent to create a new email draft in that app. This information enhances the system’s understanding of your app’s content and helps facilitate interactions with Siri, Apple Intelligence, and other system features.

To apply a schema to one of your types, add one of the following macros ahead of its declaration:

- [`AppIntent(schema:)`](appintent(schema:).md)
- [`AppEntity(schema:)`](appentity(schema:).md)
- [`AppEnum(schema:)`](appenum(schema:).md)

When you build your app, these macros expand and map the type to the schema you assign to it.

> 💡 **Tip**: Increase the number of your app’s actions that people can invoke with Apple Intelligence and Siri by adopting optional schemas.

## Topics

### Essentials
- [Making actions and content discoverable by Apple Intelligence](making-actions-and-content-discoverable-by-apple-intelligence.md)
  Equip the system so that Siri can work with your app by adding specific schemas from relevant domains.
### Markup macros
- [macro AppIntent<T>(schema: T)](appintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an schema.
- [macro AppEntity<T>(schema: T)](appentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to a schema.
- [macro AppEnum<T>(schema: T)](appenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to a schema.
### Primary domains
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
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.
### Single-purpose domains
- [Assistant](app-schema-domain-assistant.md)
  Enable people in Japan to launch your voice-based conversational app from the side button of iPhone.
- [Visual intelligence](app-schema-domain-visual-intelligence.md)
  Display search results from your app when people point the camera at relevant content.
### Shortcuts-specific domains
- [Books](app-schema-domain-books.md)
  Make your ebook reader’s actions available in the Shortcuts app by adopting schemas for common reading actions.
- [Browser](app-schema-domain-browser.md)
  Make your web browser’s actions available in the Shortcuts app by adopting schemas for common browsing actions.
- [Journaling](app-schema-domain-journaling.md)
  Make your journaling app’s actions available in the Shortcuts app by adopting schemas for journal-entry management.
- [Presentation](app-schema-domain-presentation.md)
  Make your presentation app’s actions available in the Shortcuts app by adopting schemas for common presentation actions.
- [Reader](app-schema-domain-reader.md)
  Make your document reader’s actions available in the Shortcuts app by adopting schemas for document viewing and manipulation.
- [Spreadsheet](app-schema-domain-spreadsheet.md)
  Make your spreadsheet app’s actions available in the Shortcuts app by adopting schemas for spreadsheet management.
- [Whiteboard](app-schema-domain-whiteboard.md)
  Make your whiteboard app’s actions available in the Shortcuts app by adopting schemas for common whiteboard actions.
- [Word processor](app-schema-domain-word-processor.md)
  Make your word processor’s actions available in the Shortcuts app by adopting schemas for document editing.
### Base types
- [App schema base types](app-schema-base-types.md)
  Types that provide the underlying functionality for app schemas.

## See Also

- [Visual presentation](visual-presentation.md)
  Display app intents and app entities visually using snippets, and associate intents and entities with your app’s scenes and views.
- [Donations and discovery](donations-and-discovery.md)
  Donate your app’s intents and entities to the system to help it identify trends and predict future behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domains)*