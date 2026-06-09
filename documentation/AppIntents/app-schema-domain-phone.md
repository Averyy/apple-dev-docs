# Phone

**Framework**: App Intents

Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.

#### Overview

The `.phone` domain defines app schemas that provide a structured representation for common calling actions and content. Apply schemas in the `.phone` domain to make your app’s phone functionality available to Apple Intelligence and Siri.

- **[`startCall`](appschema/phoneintent/startcall.md)**: An intent that starts calls when people say phrases like “Make a call to Bill.” or “Video call Bill and Maria.”

> 💡 **Tip**: Xcode generates a template implementation when you type `phone_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Actions
- [var startCall: some AppSchemaIntent](appschema/phoneintent/startcall.md)
  An intent schema that starts a call to a person, handle, or named group.
- [AppSchema.PhoneIntent](appschema/phoneintent.md)
  Identifies intent schemas in the phone domain.
### Content and parameter types
- [var phonePerson: some AppSchemaEntity](appschema/phoneentity/phoneperson.md)
  An entity schema for a phone person.
- [AppSchema.PhoneEntity](appschema/phoneentity.md)
  Identifies entity schemas in the phone domain.
### Types for static parameters
- [var audioVisualMode: some AppSchemaEnum](appschema/phoneenum/audiovisualmode.md)
  An enum schema for an audio visual mode parameter.
- [AppSchema.PhoneEnum](appschema/phoneenum.md)
  Identifies enum schemas in the phone domain.

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
- [Photos](app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-phone)*