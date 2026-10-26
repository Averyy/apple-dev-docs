# Messaging

**Framework**: SiriKit  
**Role**: API Collection

Send messages and search the user’s received messages.

#### Overview

With messaging intents, users can ask Siri to compose new messages, read existing messages, and indicate to other users whether they’re available.

To allow users to compose and send text or audio messages with your service, support [`INSendMessageIntent`](../Intents/insendmessageintent.md). Donate interactions when the user sends and receives messages in your app to give the system cues about which contacts to suggest in Share Sheets.

Support [`INSearchForMessagesIntent`](../Intents/insearchformessagesintent.md) and [`INSetMessageAttributeIntent`](../Intents/insetmessageattributeintent.md) to allow Siri to announce incoming messages on AirPods, and mark announced messages as [`INMessageAttribute.read`](../Intents/inmessageattribute/read.md) or [`INMessageAttribute.played`](../Intents/inmessageattribute/played.md). Adopting [`INSearchForMessagesIntent`](../Intents/insearchformessagesintent.md) also enables users to see incoming messages on a [`INCarAudioSource.sourceCarPlay`](../Intents/incaraudiosource/sourcecarplay.md)-enabled display.

![A flow diagram going from left to right. On the left is an image of a user asking Siri to send a text. In the middle is an icon of Siri sending the user’s request to an app. On the right is the text the user asked Siri to send.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3743234@2x.png)

In iOS, you can use an Intents UI app extension to display a custom message composition interface.

## Topics

### Essentials
- [Improving interactions between Siri and your messaging app](./improving-interactions-between-siri-and-your-messaging-app.md)
  Donate app-specific content, use Siri’s contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
### Sending a Message
- [protocol INSendMessageIntentHandling](../Intents/insendmessageintenthandling.md)
  An interface to handle sending messages to one or more designated users.
- [class INSendMessageIntent](../Intents/insendmessageintent.md)
  A request to send a message to the designated recipients.
- [class INSendMessageIntentResponse](../Intents/insendmessageintentresponse.md)
  Your app’s response to a send message intent.
- [enum INOutgoingMessageType](../Intents/inoutgoingmessagetype.md)
  The format of the message.
- [class INSendMessageAttachment](../Intents/insendmessageattachment.md)
  A file to include in a message.
- [class INSendMessageIntentDonationMetadata](../Intents/insendmessageintentdonationmetadata.md)
### Editing a Message
- [class INEditMessageIntent](../Intents/ineditmessageintent.md)
- [class INEditMessageIntentResponse](../Intents/ineditmessageintentresponse.md)
- [protocol INEditMessageIntentHandling](../Intents/ineditmessageintenthandling.md)
- [enum INEditMessageIntentResponseCode](../Intents/ineditmessageintentresponsecode.md)
### Unsending a Message
- [class INUnsendMessagesIntent](../Intents/inunsendmessagesintent.md)
- [class INUnsendMessagesIntentResponse](../Intents/inunsendmessagesintentresponse.md)
- [protocol INUnsendMessagesIntentHandling](../Intents/inunsendmessagesintenthandling.md)
- [enum INUnsendMessagesIntentResponseCode](../Intents/inunsendmessagesintentresponsecode.md)
### Reacting to a Message
- [enum INMessageReactionType](../Intents/inmessagereactiontype.md)
- [class INMessageLinkMetadata](../Intents/inmessagelinkmetadata.md)
- [class INMessageReaction](../Intents/inmessagereaction.md)
- [class INSticker](../Intents/insticker.md)
### Searching for Messages
- [protocol INSearchForMessagesIntentHandling](../Intents/insearchformessagesintenthandling.md)
  An interface that handles requests to search the current user’s messages.
- [class INSearchForMessagesIntent](../Intents/insearchformessagesintent.md)
  A request to list the messages that match the specified criteria.
- [class INSearchForMessagesIntentResponse](../Intents/insearchformessagesintentresponse.md)
  Your app’s response to a search for messages intent.
### Setting Message Attributes
- [protocol INSetMessageAttributeIntentHandling](../Intents/insetmessageattributeintenthandling.md)
  An interface that handles modifying message attributes.
- [class INSetMessageAttributeIntent](../Intents/insetmessageattributeintent.md)
  A request to modify the attributes of a message.
- [class INSetMessageAttributeIntentResponse](../Intents/insetmessageattributeintentresponse.md)
  Your app’s response to a set message attribute intent.
### Sharing the User’s Focus Status
- [protocol INShareFocusStatusIntentHandling](../Intents/insharefocusstatusintenthandling.md)
  A set of methods an object implements to process intents that share the user’s focus status.
- [class INShareFocusStatusIntent](../Intents/insharefocusstatusintent.md)
  An object that indicates the user’s focus status is changing.
- [class INShareFocusStatusIntentResponse](../Intents/insharefocusstatusintentresponse.md)
  Your app’s response to an intent that shares the user’s focus status.
- [enum INShareFocusStatusIntentResponseCode](../Intents/insharefocusstatusintentresponsecode.md)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
- [class INFocusStatus](../Intents/infocusstatus.md)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](../Intents/infocusstatuscenter.md)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](../Intents/infocusstatusauthorizationstatus.md)
  A constant that indicates whether your app has authorization to access the user’s focus status.
### Managing Message Information
- [class INMessage](../Intents/inmessage.md)
  An object that describes a sent or received message.
- [enum INMessageAttribute](../Intents/inmessageattribute.md)
  Constants that indicate an attribute of a message.
- [struct INMessageAttributeOptions](../Intents/inmessageattributeoptions.md)
  Constants that indicate a message search filter.
- [class INPerson](../Intents/inperson.md)
  Information about a person participating in a SiriKit interaction.
### Providing Resolution Results
- [class INMessageAttributeResolutionResult](../Intents/inmessageattributeresolutionresult.md)
  A resolution result for assorted attributes of a message.
- [class INMessageAttributeOptionsResolutionResult](../Intents/inmessageattributeoptionsresolutionresult.md)
  A resolution result for a search parameter that filters by message status.
- [class INDateComponentsRangeResolutionResult](../Intents/indatecomponentsrangeresolutionresult.md)
  A resolution result for a range of dates in a parameter of an intent.
- [class INSendMessageRecipientResolutionResult](../Intents/insendmessagerecipientresolutionresult.md)
  A resolution result for the recipient of a message.
- [class INPersonResolutionResult](../Intents/inpersonresolutionresult.md)
  A resolution result for a user as a parameter of an intent.
- [class INOutgoingMessageTypeResolutionResult](../Intents/inoutgoingmessagetyperesolutionresult.md)
  A resolution result for the message’s format.

## See Also

### Standard Intents
- [Car Commands](./car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Lists and Notes](./lists-and-notes.md)
  Create and manage notes and to-do list items.
- [Media](./media.md)
  Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.
- [Payments](./payments.md)
  Send payments between users or pay bills.
- [Restaurant Reservations](./restaurant-reservations.md)
  Create and manage restaurant reservations with help from the Maps app.
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/messaging)*