# Messaging

**Framework**: SiriKit  
**Role**: API Collection

Send messages and search the user’s received messages.

#### Overview

With messaging intents, users can ask Siri to compose new messages, read existing messages, and indicate to other users whether they’re available.

To allow users to compose and send text or audio messages with your service, support [`INSendMessageIntent`](https://developer.apple.com/documentation/intents/insendmessageintent). Donate interactions when the user sends and receives messages in your app to give the system cues about which contacts to suggest in Share Sheets.

Support [`INSearchForMessagesIntent`](https://developer.apple.com/documentation/intents/insearchformessagesintent) and [`INSetMessageAttributeIntent`](https://developer.apple.com/documentation/intents/insetmessageattributeintent) to allow Siri to announce incoming messages on AirPods, and mark announced messages as [`INMessageAttribute.read`](https://developer.apple.com/documentation/intents/inmessageattribute/read) or [`INMessageAttribute.played`](https://developer.apple.com/documentation/intents/inmessageattribute/played). Adopting [`INSearchForMessagesIntent`](https://developer.apple.com/documentation/intents/insearchformessagesintent) also enables users to see incoming messages on a [`INCarAudioSource.sourceCarPlay`](https://developer.apple.com/documentation/intents/incaraudiosource/sourcecarplay)-enabled display.

![A flow diagram going from left to right. On the left is an image of a user asking Siri to send a text. In the middle is an icon of Siri sending the user’s request to an app. On the right is the text the user asked Siri to send.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3743234@2x.png)

In iOS, you can use an Intents UI app extension to display a custom message composition interface.

## Topics

### Essentials
- [Improving interactions between Siri and your messaging app](./improving-interactions-between-siri-and-your-messaging-app.md)
  Donate app-specific content, use Siri’s contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
### Sending a Message
- [protocol INSendMessageIntentHandling](https://developer.apple.com/documentation/intents/insendmessageintenthandling)
  An interface to handle sending messages to one or more designated users.
- [class INSendMessageIntent](https://developer.apple.com/documentation/intents/insendmessageintent)
  A request to send a message to the designated recipients.
- [class INSendMessageIntentResponse](https://developer.apple.com/documentation/intents/insendmessageintentresponse)
  Your app’s response to a send message intent.
- [enum INOutgoingMessageType](https://developer.apple.com/documentation/intents/inoutgoingmessagetype)
  The format of the message.
- [class INSendMessageAttachment](https://developer.apple.com/documentation/intents/insendmessageattachment)
  A file to include in a message.
- [class INSendMessageIntentDonationMetadata](https://developer.apple.com/documentation/intents/insendmessageintentdonationmetadata)
### Editing a Message
- [class INEditMessageIntent](https://developer.apple.com/documentation/intents/ineditmessageintent)
- [class INEditMessageIntentResponse](https://developer.apple.com/documentation/intents/ineditmessageintentresponse)
- [protocol INEditMessageIntentHandling](https://developer.apple.com/documentation/intents/ineditmessageintenthandling)
- [enum INEditMessageIntentResponseCode](https://developer.apple.com/documentation/intents/ineditmessageintentresponsecode)
### Unsending a Message
- [class INUnsendMessagesIntent](https://developer.apple.com/documentation/intents/inunsendmessagesintent)
- [class INUnsendMessagesIntentResponse](https://developer.apple.com/documentation/intents/inunsendmessagesintentresponse)
- [protocol INUnsendMessagesIntentHandling](https://developer.apple.com/documentation/intents/inunsendmessagesintenthandling)
- [enum INUnsendMessagesIntentResponseCode](https://developer.apple.com/documentation/intents/inunsendmessagesintentresponsecode)
### Reacting to a Message
- [enum INMessageReactionType](https://developer.apple.com/documentation/intents/inmessagereactiontype)
- [class INMessageLinkMetadata](https://developer.apple.com/documentation/intents/inmessagelinkmetadata)
- [class INMessageReaction](https://developer.apple.com/documentation/intents/inmessagereaction)
- [class INSticker](https://developer.apple.com/documentation/intents/insticker)
### Searching for Messages
- [protocol INSearchForMessagesIntentHandling](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling)
  An interface that handles requests to search the current user’s messages.
- [class INSearchForMessagesIntent](https://developer.apple.com/documentation/intents/insearchformessagesintent)
  A request to list the messages that match the specified criteria.
- [class INSearchForMessagesIntentResponse](https://developer.apple.com/documentation/intents/insearchformessagesintentresponse)
  Your app’s response to a search for messages intent.
### Setting Message Attributes
- [protocol INSetMessageAttributeIntentHandling](https://developer.apple.com/documentation/intents/insetmessageattributeintenthandling)
  An interface that handles modifying message attributes.
- [class INSetMessageAttributeIntent](https://developer.apple.com/documentation/intents/insetmessageattributeintent)
  A request to modify the attributes of a message.
- [class INSetMessageAttributeIntentResponse](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponse)
  Your app’s response to a set message attribute intent.
### Sharing the User’s Focus Status
- [protocol INShareFocusStatusIntentHandling](https://developer.apple.com/documentation/intents/insharefocusstatusintenthandling)
  A set of methods an object implements to process intents that share the user’s focus status.
- [class INShareFocusStatusIntent](https://developer.apple.com/documentation/intents/insharefocusstatusintent)
  An object that indicates the user’s focus status is changing.
- [class INShareFocusStatusIntentResponse](https://developer.apple.com/documentation/intents/insharefocusstatusintentresponse)
  Your app’s response to an intent that shares the user’s focus status.
- [enum INShareFocusStatusIntentResponseCode](https://developer.apple.com/documentation/intents/insharefocusstatusintentresponsecode)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
- [class INFocusStatus](https://developer.apple.com/documentation/intents/infocusstatus)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](https://developer.apple.com/documentation/intents/infocusstatuscenter)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](https://developer.apple.com/documentation/intents/infocusstatusauthorizationstatus)
  A constant that indicates whether your app has authorization to access the user’s focus status.
### Managing Message Information
- [class INMessage](https://developer.apple.com/documentation/intents/inmessage)
  An object that describes a sent or received message.
- [enum INMessageAttribute](https://developer.apple.com/documentation/intents/inmessageattribute)
  Constants that indicate an attribute of a message.
- [struct INMessageAttributeOptions](https://developer.apple.com/documentation/intents/inmessageattributeoptions)
  Constants that indicate a message search filter.
- [class INPerson](https://developer.apple.com/documentation/intents/inperson)
  Information about a person participating in a SiriKit interaction.
### Providing Resolution Results
- [class INMessageAttributeResolutionResult](https://developer.apple.com/documentation/intents/inmessageattributeresolutionresult)
  A resolution result for assorted attributes of a message.
- [class INMessageAttributeOptionsResolutionResult](https://developer.apple.com/documentation/intents/inmessageattributeoptionsresolutionresult)
  A resolution result for a search parameter that filters by message status.
- [class INDateComponentsRangeResolutionResult](https://developer.apple.com/documentation/intents/indatecomponentsrangeresolutionresult)
  A resolution result for a range of dates in a parameter of an intent.
- [class INSendMessageRecipientResolutionResult](https://developer.apple.com/documentation/intents/insendmessagerecipientresolutionresult)
  A resolution result for the recipient of a message.
- [class INPersonResolutionResult](https://developer.apple.com/documentation/intents/inpersonresolutionresult)
  A resolution result for a user as a parameter of an intent.
- [class INOutgoingMessageTypeResolutionResult](https://developer.apple.com/documentation/intents/inoutgoingmessagetyperesolutionresult)
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