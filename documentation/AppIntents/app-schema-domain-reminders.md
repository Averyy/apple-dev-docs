# Reminders

**Framework**: App Intents

Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.

#### Overview

The `.reminders` domain defines app schemas that provide a structured representation for common reminder actions and content. Apply schemas in the `.reminders` domain to make your app’s reminder functionality available to Apple Intelligence and Siri. Each schema defines the requirements for intents, parameters, and results so people get a consistent experience across reminder apps. For example, a person can create a reminder on different apps that support the [`createReminder`](appschema/remindersintent/createreminder.md) schema with the same phrases.

The following table maps example phrases that apply to each schema:

| Reminders intent schemas | Example phrases |
| --- | --- |
| [`createList`](appschema/remindersintent/createlist.md) | “Create a list called shopping.” |
| [`createReminder`](appschema/remindersintent/createreminder.md) | “Create a reminder.” or “Create a reminder called vote.” |
| [`createSection`](appschema/remindersintent/createsection.md) | “Create a section called vegetables.” |
| [`deleteReminders`](appschema/remindersintent/deletereminders.md) | “Delete this reminder.” |
| [`updateReminder`](appschema/remindersintent/updatereminder.md) | “Mark this reminder as completed.” or “Set the due date for this reminder to tomorrow.” |

> 💡 **Tip**: Xcode generates a template implementation when you type `reminders_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Actions
- [var createList: some AppSchemaIntent](appschema/remindersintent/createlist.md)
  An intent schema that creates a new reminder list.
- [var createReminder: some AppSchemaIntent](appschema/remindersintent/createreminder.md)
  An intent schema that creates a new reminder.
- [var createSection: some AppSchemaIntent](appschema/remindersintent/createsection.md)
  An intent schema that creates a new reminder list section.
- [var deleteReminders: some AppSchemaIntent](appschema/remindersintent/deletereminders.md)
  An intent schema that deletes reminders.
- [var updateGroup: some AppSchemaIntent](appschema/remindersintent/updategroup.md)
  An intent schema that updates a reminder list group.
- [var updateList: some AppSchemaIntent](appschema/remindersintent/updatelist.md)
  An intent schema that updates a reminder list.
- [var updateReminder: some AppSchemaIntent](appschema/remindersintent/updatereminder.md)
  An intent schema that updates a reminder.
- [var updateSection: some AppSchemaIntent](appschema/remindersintent/updatesection.md)
  An intent schema that updates a reminder list section.
### Content and parameter types
- [var group: some AppSchemaEntity](appschema/remindersentity/group.md)
  An entity schema for a group.
- [var list: some AppSchemaEntity](appschema/remindersentity/list.md)
  An entity schema for a list.
- [var locationTrigger: some AppSchemaEntity](appschema/remindersentity/locationtrigger.md)
  An entity schema for a location trigger.
- [var reminder: some AppSchemaEntity](appschema/remindersentity/reminder.md)
  An entity schema for a reminder.
- [var section: some AppSchemaEntity](appschema/remindersentity/section.md)
  An entity schema for a section.
- [AppSchema.RemindersEntity](appschema/remindersentity.md)
  Identifies entity schemas in the reminders domain.
### Types for static parameters
- [var listType: some AppSchemaEnum](appschema/remindersenum/listtype.md)
  An enum schema for a list type parameter.
- [var locationTriggerEvent: some AppSchemaEnum](appschema/remindersenum/locationtriggerevent.md)
  An enum schema for a location trigger event parameter.
- [AppSchema.RemindersEnum](appschema/remindersenum.md)
  Identifies enum schemas in the reminders domain.

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
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-reminders)*