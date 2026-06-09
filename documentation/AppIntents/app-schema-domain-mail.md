# Mail

**Framework**: App Intents

Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.

#### Overview

The `.mail` domain defines app schemas that provide a structured representation for common email actions and content. Apply schemas in the `.mail` domain to make your app’s email functionality available to Apple Intelligence and Siri. Each schema defines the requirements for intents, parameters, and results so people get a consistent experience across email apps. For example, a person can compose an email on different apps that support the [`createDraft`](appschema/mailintent/createdraft.md) schema with the same phrases.

The following table maps example phrases that apply to each schema. Your app needs to support all of these schemas when it supports any one of them.

| Mail intent schemas | Example phrases |
| --- | --- |
| [`createDraft`](appschema/mailintent/createdraft.md) | “Compose a mail.” or “Write an email to example@example.com about photos from team dinner.” |
| [`updateDraft`](appschema/mailintent/updatedraft.md) | “Add example@example.com to recipients.” or “Set subject to coffee session.” |
| [`saveDraft`](appschema/mailintent/savedraft.md) | “Draft this email for later.” or “Save it.” |
| [`openDraft`](appschema/mailintent/opendraft.md) | “Open the draft email to John and James.” |
| [`deleteDraft`](appschema/mailintent/deletedraft.md) | “Delete this draft.” or “Trash my most recent draft.” |
| [`sendDraft`](appschema/mailintent/senddraft.md) | “Send this email.” or “Send this email tomorrow at 9 PM.” |
| [`openMessage`](appschema/mailintent/openmessage.md) | “Open the email about team offsite instructions.” |
| [`replyMail`](appschema/mailintent/replymail.md) | “Reply to an email.” or “Reply to mail thread with my manager.” |
| [`forwardMail`](appschema/mailintent/forwardmail.md) | “Forward an email.” or “Forward the email about the baseball schedule to John Appleseed.” |
| [`updateMail`](appschema/mailintent/updatemail.md) | “Mark this email as read.” or “Flag this email.” |
| [`archiveMail`](appschema/mailintent/archivemail.md) | “Archive book club emails.” or “Archive emails from Nancy.” |
| [`deleteMail`](appschema/mailintent/deletemail.md) | “Delete emails from Julian.” or “Trash all mail messages from Example Store.” |

At build time, Xcode validates whether your app implements all the schemas in the group.

> 💡 **Tip**: Xcode generates a template implementation when you type `mail_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Actions
- [var archiveMail: some AppSchemaIntent](appschema/mailintent/archivemail.md)
  An intent schema that archives one or more email messages.
- [var createDraft: some AppSchemaIntent](appschema/mailintent/createdraft.md)
  An intent schema that opens an email composer to draft an email.
- [var deleteDraft: some AppSchemaIntent](appschema/mailintent/deletedraft.md)
  An intent schema that deletes one or more email drafts.
- [var deleteMail: some AppSchemaIntent](appschema/mailintent/deletemail.md)
  An intent schema that deletes one or more email messages.
- [var forwardMail: some AppSchemaIntent](appschema/mailintent/forwardmail.md)
  An intent schema that opens an email composer to forward an email.
- [var openDraft: some AppSchemaIntent](appschema/mailintent/opendraft.md)
  An intent schema that opens an email draft.
- [var openMessage: some AppSchemaIntent](appschema/mailintent/openmessage.md)
  An intent schema that opens an email message.
- [var replyMail: some AppSchemaIntent](appschema/mailintent/replymail.md)
  An intent schema that opens an email composer to reply to an email.
- [var saveDraft: some AppSchemaIntent](appschema/mailintent/savedraft.md)
  An intent schema that saves an email draft.
- [var sendDraft: some AppSchemaIntent](appschema/mailintent/senddraft.md)
  An intent schema that sends an email draft or schedules it to be sent later.
- [var updateDraft: some AppSchemaIntent](appschema/mailintent/updatedraft.md)
  An intent schema that makes updates to an email draft.
- [var updateMail: some AppSchemaIntent](appschema/mailintent/updatemail.md)
  An intent schema that makes updates to one or more existing email messages by modifying the status, flags, and location.
- [AppSchema.MailIntent](appschema/mailintent.md)
  Identifies intent schemas in the mail domain.
### Content and parameter types
- [var account: some AppSchemaEntity](appschema/mailentity/account.md)
  An entity schema for an account.
- [var draft: some AppSchemaEntity](appschema/mailentity/draft.md)
  An entity schema for a draft.
- [var mailbox: some AppSchemaEntity](appschema/mailentity/mailbox.md)
  An entity schema for a mailbox.
- [var message: some AppSchemaEntity](appschema/mailentity/message.md)
  An entity schema for a message.
- [var thread: some AppSchemaEntity](appschema/mailentity/thread.md)
  An entity schema for a thread.
- [AppSchema.MailEntity](appschema/mailentity.md)
  Identifies entity schemas in the mail domain.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-mail)*