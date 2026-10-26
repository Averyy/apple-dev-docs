# VoIP Calling

**Framework**: SiriKit  
**Role**: API Collection

Initiate calls and search the user’s call history.

#### Overview

With the VoIP domain, users can ask Siri to initiate audio and video calls or search for calls already received by your app. Your Intents app extension validates the intent parameters, but doesn’t place calls or perform searches directly. Instead, SiriKit expects you to hand off control to your app, which is responsible for displaying the search results and managing calls.

> ❗ **Important**:  It’s strongly recommended that you use CallKit to initiate and manage your app’s calls. CallKit lets you integrate your calling services with the system, making it easier for users to receive and manage calls from your app and other calling apps. If you don’t support CallKit, Siri launches your app so it can begin the call.

## Topics

### Starting a Call
- [protocol INStartCallIntentHandling](../Intents/instartcallintenthandling.md)
  An interface that handles requests to start audio and video calls.
- [class INStartCallIntent](../Intents/instartcallintent.md)
  A request to start an audio or video call with one or more users.
- [class INStartCallIntentResponse](../Intents/instartcallintentresponse.md)
  Your app’s response to a start call intent.
- [enum INStartCallCallRecordToCallBackUnsupportedReason](../Intents/instartcallcallrecordtocallbackunsupportedreason.md)
  A reason why your app can’t use a record to call a person back.
### Answering a Call
- [class INAnswerCallIntent](../Intents/inanswercallintent.md)
- [class INAnswerCallIntentResponse](../Intents/inanswercallintentresponse.md)
- [protocol INAnswerCallIntentHandling](../Intents/inanswercallintenthandling.md)
- [enum INAnswerCallIntentResponseCode](../Intents/inanswercallintentresponsecode.md)
### Describing a Call
- [class INCallRecord](../Intents/incallrecord.md)
  The details about a call handled by your app.
- [class INCallGroup](../Intents/incallgroup.md)
  The details of a group call handled by your app.
- [class INCallRecordFilter](../Intents/incallrecordfilter.md)
  Filters a user specifies to redial a call.
- [enum INCallRecordType](../Intents/incallrecordtype.md)
  Constants describing the type of the call.
- [struct INCallRecordTypeOptions](../Intents/incallrecordtypeoptions.md)
  Constants describing the types of calls to include during a search.
- [enum INCallDestinationType](../Intents/incalldestinationtype.md)
  Constants describing the destination of a call.
### Ending a Call
- [class INHangUpCallIntent](../Intents/inhangupcallintent.md)
- [class INHangUpCallIntentResponse](../Intents/inhangupcallintentresponse.md)
- [protocol INHangUpCallIntentHandling](../Intents/inhangupcallintenthandling.md)
- [enum INHangUpCallIntentResponseCode](../Intents/inhangupcallintentresponsecode.md)
### Resolution Results
- [class INCallRecordResolutionResult](../Intents/incallrecordresolutionresult.md)
  A resolution result for the details of a call.
- [class INCallRecordTypeResolutionResult](../Intents/incallrecordtyperesolutionresult.md)
  A resolution result for the types of calls that your app handled.
- [class INCallDestinationTypeResolutionResult](../Intents/incalldestinationtyperesolutionresult.md)
  A resolution result for the destination type of a call.
- [class INCallCapabilityResolutionResult](../Intents/incallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.
- [class INCallRecordTypeOptionsResolutionResult](../Intents/incallrecordtypeoptionsresolutionresult.md)
  A resolution result for the call types to include in a search.
- [class INStartCallContactResolutionResult](../Intents/instartcallcontactresolutionresult.md)
  A resolution result for the contact for the call.
- [class INStartCallCallCapabilityResolutionResult](../Intents/instartcallcallcapabilityresolutionresult.md)
  A resolution result for the call capability for the call.
- [class INStartCallCallRecordToCallBackResolutionResult](../Intents/instartcallcallrecordtocallbackresolutionresult.md)
  A resolution result for the redial capabilities of a missed call.
### Sharing the User’s Focus Status
- [protocol INShareFocusStatusIntentHandling](../Intents/insharefocusstatusintenthandling.md)
  A set of methods an object implements to process intents that share the user’s focus status.
- [class INShareFocusStatusIntent](../Intents/insharefocusstatusintent.md)
  An object that indicates the user’s focus status is changing.
- [class INShareFocusStatusIntentResponse](../Intents/insharefocusstatusintentresponse.md)
  Your app’s response to an intent that shares the user’s focus status.
- [class INFocusStatus](../Intents/infocusstatus.md)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](../Intents/infocusstatuscenter.md)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](../Intents/infocusstatusauthorizationstatus.md)
  A constant that indicates whether your app has authorization to access the user’s focus status.
- [enum INShareFocusStatusIntentResponseCode](../Intents/insharefocusstatusintentresponsecode.md)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
### Specifying Search Options
- [struct INCallCapabilityOptions](../Intents/incallcapabilityoptions.md)
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