# VoIP Calling

**Framework**: SiriKit  
**Role**: API Collection

Initiate calls and search the user’s call history.

#### Overview

With the VoIP domain, users can ask Siri to initiate audio and video calls or search for calls already received by your app. Your Intents app extension validates the intent parameters, but doesn’t place calls or perform searches directly. Instead, SiriKit expects you to hand off control to your app, which is responsible for displaying the search results and managing calls.

> ❗ **Important**:  It’s strongly recommended that you use CallKit to initiate and manage your app’s calls. CallKit lets you integrate your calling services with the system, making it easier for users to receive and manage calls from your app and other calling apps. If you don’t support CallKit, Siri launches your app so it can begin the call.

## Topics

### Starting a Call
- [protocol INStartCallIntentHandling](https://developer.apple.com/documentation/intents/instartcallintenthandling)
  An interface that handles requests to start audio and video calls.
- [class INStartCallIntent](https://developer.apple.com/documentation/intents/instartcallintent)
  A request to start an audio or video call with one or more users.
- [class INStartCallIntentResponse](https://developer.apple.com/documentation/intents/instartcallintentresponse)
  Your app’s response to a start call intent.
- [enum INStartCallCallRecordToCallBackUnsupportedReason](https://developer.apple.com/documentation/intents/instartcallcallrecordtocallbackunsupportedreason)
  A reason why your app can’t use a record to call a person back.
### Answering a Call
- [class INAnswerCallIntent](https://developer.apple.com/documentation/intents/inanswercallintent)
- [class INAnswerCallIntentResponse](https://developer.apple.com/documentation/intents/inanswercallintentresponse)
- [protocol INAnswerCallIntentHandling](https://developer.apple.com/documentation/intents/inanswercallintenthandling)
- [enum INAnswerCallIntentResponseCode](https://developer.apple.com/documentation/intents/inanswercallintentresponsecode)
### Describing a Call
- [class INCallRecord](https://developer.apple.com/documentation/intents/incallrecord)
  The details about a call handled by your app.
- [class INCallGroup](https://developer.apple.com/documentation/intents/incallgroup)
  The details of a group call handled by your app.
- [class INCallRecordFilter](https://developer.apple.com/documentation/intents/incallrecordfilter)
  Filters a user specifies to redial a call.
- [enum INCallRecordType](https://developer.apple.com/documentation/intents/incallrecordtype)
  Constants describing the type of the call.
- [struct INCallRecordTypeOptions](https://developer.apple.com/documentation/intents/incallrecordtypeoptions)
  Constants describing the types of calls to include during a search.
- [enum INCallDestinationType](https://developer.apple.com/documentation/intents/incalldestinationtype)
  Constants describing the destination of a call.
### Ending a Call
- [class INHangUpCallIntent](https://developer.apple.com/documentation/intents/inhangupcallintent)
- [class INHangUpCallIntentResponse](https://developer.apple.com/documentation/intents/inhangupcallintentresponse)
- [protocol INHangUpCallIntentHandling](https://developer.apple.com/documentation/intents/inhangupcallintenthandling)
- [enum INHangUpCallIntentResponseCode](https://developer.apple.com/documentation/intents/inhangupcallintentresponsecode)
### Resolution Results
- [class INCallRecordResolutionResult](https://developer.apple.com/documentation/intents/incallrecordresolutionresult)
  A resolution result for the details of a call.
- [class INCallRecordTypeResolutionResult](https://developer.apple.com/documentation/intents/incallrecordtyperesolutionresult)
  A resolution result for the types of calls that your app handled.
- [class INCallDestinationTypeResolutionResult](https://developer.apple.com/documentation/intents/incalldestinationtyperesolutionresult)
  A resolution result for the destination type of a call.
- [class INCallCapabilityResolutionResult](https://developer.apple.com/documentation/intents/incallcapabilityresolutionresult)
  A resolution result for the call capability for the call.
- [class INCallRecordTypeOptionsResolutionResult](https://developer.apple.com/documentation/intents/incallrecordtypeoptionsresolutionresult)
  A resolution result for the call types to include in a search.
- [class INStartCallContactResolutionResult](https://developer.apple.com/documentation/intents/instartcallcontactresolutionresult)
  A resolution result for the contact for the call.
- [class INStartCallCallCapabilityResolutionResult](https://developer.apple.com/documentation/intents/instartcallcallcapabilityresolutionresult)
  A resolution result for the call capability for the call.
- [class INStartCallCallRecordToCallBackResolutionResult](https://developer.apple.com/documentation/intents/instartcallcallrecordtocallbackresolutionresult)
  A resolution result for the redial capabilities of a missed call.
### Sharing the User’s Focus Status
- [protocol INShareFocusStatusIntentHandling](https://developer.apple.com/documentation/intents/insharefocusstatusintenthandling)
  A set of methods an object implements to process intents that share the user’s focus status.
- [class INShareFocusStatusIntent](https://developer.apple.com/documentation/intents/insharefocusstatusintent)
  An object that indicates the user’s focus status is changing.
- [class INShareFocusStatusIntentResponse](https://developer.apple.com/documentation/intents/insharefocusstatusintentresponse)
  Your app’s response to an intent that shares the user’s focus status.
- [class INFocusStatus](https://developer.apple.com/documentation/intents/infocusstatus)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](https://developer.apple.com/documentation/intents/infocusstatuscenter)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](https://developer.apple.com/documentation/intents/infocusstatusauthorizationstatus)
  A constant that indicates whether your app has authorization to access the user’s focus status.
- [enum INShareFocusStatusIntentResponseCode](https://developer.apple.com/documentation/intents/insharefocusstatusintentresponsecode)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
### Specifying Search Options
- [struct INCallCapabilityOptions](https://developer.apple.com/documentation/intents/incallcapabilityoptions)
  Constants indicating the capabilities of the call.

## See Also

### Standard Intents
- [Car Commands](./car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Lists and Notes](./lists-and-notes.md)
  Create and manage notes and to-do list items.
- [Media](./media.md)
  Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.
- [Messaging](./messaging.md)
  Send messages and search the user’s received messages.
- [Payments](./payments.md)
  Send payments between users or pay bills.
- [Restaurant Reservations](./restaurant-reservations.md)
  Create and manage restaurant reservations with help from the Maps app.
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/voip-calling)*