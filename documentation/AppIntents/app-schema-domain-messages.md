# Messages

**Framework**: App Intents

Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.

#### Overview

The `.messages` domain defines app schemas that provide a structured representation for common messaging actions and content. Apply schemas in the `.messages` domain to make your app’s messaging functionality available to Apple Intelligence and Siri. Each schema defines the requirements for intents, parameters, and results so people get a consistent experience across messaging apps. For example, a person can send a message on different apps that support the [`sendMessage`](appschema/messagesintent/sendmessage.md) schema with the same phrases.

The following table maps example phrases that apply to each schema. Your app needs to support all of these schemas when it supports any one of them.

| Messages intent schemas | Example phrases |
| --- | --- |
| [`draftMessage`](appschema/messagesintent/draftmessage.md) | “Start a message.” or “Draft a message.” |
| [`sendMessage`](appschema/messagesintent/sendmessage.md) | “Send a message to John asking what time the party starts.” or “Text the foodie group and ask, ‘What time is dinner again?’” |
| [`editSentMessage`](appschema/messagesintent/editsentmessage.md) | “Edit my last message.” or “Edit my last message to say ‘Good morning!’ instead of ‘Hello!’” |
| [`unsendMessage`](appschema/messagesintent/unsendmessage.md) | “Unsend my last message.” or “Unsend that.” |
| [`setMessageReadStatus`](appschema/messagesintent/setmessagereadstatus.md) | “Mark this message as unread.” or “Mark the message from the lawyer as unread.” |

At build time, Xcode validates whether your app implements all the schemas in the group.

> 💡 **Tip**: Xcode generates a template implementation when you type `messages_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Essentials
- [Integrating your messaging app with Apple Intelligence](integrating-your-messaging-app-with-apple-intelligence.md)
  Adopt message schemas so people can send messages and manage conversations with Siri.
### Actions
- [var draftMessage: some AppSchemaIntent](appschema/messagesintent/draftmessage.md)
  An intent schema that opens app to start or continue composing a message via touch.
- [var editSentMessage: some AppSchemaIntent](appschema/messagesintent/editsentmessage.md)
  An intent schema that edits an already sent message with new content.
- [var sendMessage: some AppSchemaIntent](appschema/messagesintent/sendmessage.md)
  An intent schema that sends a message with the associated parameters.
- [var setMessageReadStatus: some AppSchemaIntent](appschema/messagesintent/setmessagereadstatus.md)
  An intent schema that changes the message read status to a given value.
- [var unsendMessage: some AppSchemaIntent](appschema/messagesintent/unsendmessage.md)
  An intent schema that unsends a sent message.
- [AppSchema.MessagesIntent](appschema/messagesintent.md)
  Identifies intent schemas in the messages domain.
### Content and parameter types
- [var conversation: some AppSchemaEntity](appschema/messagesentity/conversation.md)
  An entity schema for a conversation.
- [var customAttachment: some AppSchemaEntity](appschema/messagesentity/customattachment.md)
  An entity schema for a custom attachment.
- [var message: some AppSchemaEntity](appschema/messagesentity/message.md)
  An entity schema for a message.
- [var messagePerson: some AppSchemaEntity](appschema/messagesentity/messageperson.md)
  An entity schema for a message person.
- [AppSchema.MessagesEntity](appschema/messagesentity.md)
  Identifies entity schemas in the messages domain.
### Types for static parameters
- [var conversationAttribute: some AppSchemaEnum](appschema/messagesenum/conversationattribute.md)
  An enum schema for a conversation attribute parameter.
- [var customReaction: some AppSchemaEnum](appschema/messagesenum/customreaction.md)
  An enum schema for a custom reaction parameter.
- [var messageAttribute: some AppSchemaEnum](appschema/messagesenum/messageattribute.md)
  An enum schema for a message attribute parameter.
- [var messageEffect: some AppSchemaEnum](appschema/messagesenum/messageeffect.md)
  An enum schema for a message effect parameter.
- [var messageType: some AppSchemaEnum](appschema/messagesenum/messagetype.md)
  An enum schema for a message type parameter.
- [AppSchema.MessagesEnum](appschema/messagesenum.md)
  Identifies enum schemas in the messages domain.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-messages)*