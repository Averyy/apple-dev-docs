# App intent domains

**Framework**: App Intents

Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.

#### Overview

To enable enhanced understanding and more conversational interactions with Siri for your app, choose a domain and a schema that match your app’s functionality. By conforming your app intent, app entity, or your app enumeration to a schema, you ensure that Apple Intelligence understands your app’s actions and content. When you’ve identified the schema to use, leverage the [`AppIntent(schema:)`](appintent(schema:).md), [`AppEntity(schema:)`](appentity(schema:).md), and [`AppEnum(schema:)`](appenum(schema:).md) macros to write schema-conforming code.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

To learn more, refer to [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md) and [`Making onscreen content available to Siri and Apple Intelligence`](making-onscreen-content-available-to-siri-and-apple-intelligence.md).

## Topics

### Domains
- [Assistant](app-intent-domain-assistant.md)
  An app intent schema that lets people in Japan configure the side button of iPhone to launch your voice-based conversational app.
- [Books](app-intent-domain-books.md)
  App intent schemas you use for ebook reader functionality and content.
- [Browser](app-intent-domain-browser.md)
  App intent schemas you use for web browsing functionality and content.
- [Camera](app-intent-domain-camera.md)
  App intent schemas you use for camera functionality and content.
- [File management](app-intent-domain-file-management.md)
  App intent schemas you use for file management functionality and content.
- [Journaling](app-intent-domain-journaling.md)
  App intent schemas you use for journaling functionality and content.
- [Mail](app-intent-domain-mail.md)
  App intent schemas you use for email clients.
- [Photos](app-intent-domain-photos.md)
  App intent schemas you use for photo and video functionality and content.
- [Presentations](app-intent-domain-presentation.md)
  App intent schemas you use for presentation functionality and content.
- [Reader](app-intent-domain-reader.md)
  App intent schemas you use for document reading functionality and content.
- [Spreadsheet](app-intent-domain-spreadsheet.md)
  App intent schemas you use for spreadsheet functionality and content.
- [System and in-app search](app-intent-domain-system-and-search.md)
  App intent schemas you use for in-app search functionality and content.
- [Visual intelligence](app-intent-domain-visual-intelligence.md)
  An app intent schema that lets you integrate your app with visual intelligence.
- [Whiteboard](app-intent-domain-whiteboard.md)
  App intent schemas you use for whiteboard functionality and content.
- [Word proccessor](app-intent-domain-wordprocessor.md)
  App intent schemas you use for text editing functionality and content.
### Macros
- [macro AppIntent<T>(schema: T)](appintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an schema.
- [macro AppEntity<T>(schema: T)](appentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to a schema.
- [macro AppEnum<T>(schema: T)](appenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to a schema.
### Base protocols
- [Assistant schema base protocols](assistant-schema-base-protocols.md)
  Protocols that provide the underlying functionality for assistant schemas.
### Deprecated macros
- [macro AssistantIntent<T>(schema: T)](assistantintent(schema:).md)
  A Swift macro you use to make sure your app intent conforms to an assistant schema.
- [macro AssistantEntity<T>(schema: T)](assistantentity(schema:).md)
  A Swift macro you use to make sure your app entity conforms to an assistant schema.
- [macro AssistantEnum<T>(schema: T)](assistantenum(schema:).md)
  A Swift macro you use to make sure your app enum conforms to an assistant schema.

## See Also

- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [App intents](app-intents.md)
  Define the custom actions your app exposes to the system using specialized intents.
- [Intent infrastructure](intent-infrastructure.md)
  Provide supplemental context for your intents, and create infrastructure to make app intents reusable across your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-intent-domains)*