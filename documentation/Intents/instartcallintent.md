# INStartCallIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to start an audio or video call with one or more users.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INStartCallIntent
```

```objc
@interface INStartCallIntent : INIntent
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

#### Overview

SiriKit creates [`INStartCallIntent`](./instartcallintent.md) objects when the user wants to place a call using your app. A call intent object contains either the users to call or redialing information. It’s up to you to match the information in this object to contacts in your app and initiate the resulting call.

Your Intents extension receives this intent when the user tries to initiate a call from the Siri interface. If your app supports CallKit, you may also receive this intent when the user tries to initiate a call from system interfaces, such as the Recents tab of the Phone app.

To handle this intent, the handler object in your Intents extension must adopt the [`INStartCallIntentHandling`](./instartcallintenthandling.md) protocol. Your handler should confirm the request and create an [`INStartCallIntentResponse`](./instartcallintentresponse.md) object that indicates it’s possible to begin the call. Don’t try to initiate calls directly from your Intents extension. Instead, SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that your app must then use to initiate the call. SiriKit places an [`INInteraction`](./ininteraction.md) object in the user activity object with this intent. For calls initiated through Siri, the interaction object also includes the response provided by your Intents extension.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | No |

## Topics

### Initializing the Intent Object
- [convenience init(audioRoute: INCallAudioRoute, destinationType: INCallDestinationType, contacts: [INPerson]?, recordTypeForRedialing: INCallRecordType, callCapability: INCallCapability)](./instartcallintent/init%28audioroute,destinationtype,contacts,recordtypeforredialing,callcapability%29.md)
  Creates a start call intent object with the specified parameters.
- [init(callRecordFilter: INCallRecordFilter?, callRecordToCallBack: INCallRecord?, audioRoute: INCallAudioRoute, destinationType: INCallDestinationType, contacts: [INPerson]?, callCapability: INCallCapability)](./instartcallintent/init%28callrecordfilter,callrecordtocallback,audioroute,destinationtype,contacts,callcapability%29.md)
  Creates a start call intent object with the specified parameters.
### Getting the Call Details
- [var callCapability: INCallCapability](./instartcallintent/callcapability.md)
  The type of call the user initiated.
- [var contacts: [INPerson]?](./instartcallintent/contacts.md)
  The users to call.
- [var destinationType: INCallDestinationType](./instartcallintent/destinationtype.md)
  The type of call to place.
- [var audioRoute: INCallAudioRoute](./instartcallintent/audioroute.md)
  The audio route the call is using.
- [var recordTypeForRedialing: INCallRecordType](./instartcallintent/recordtypeforredialing.md)
  The category of past call record contact information used for redialing.
- [var callRecordFilter: INCallRecordFilter?](./instartcallintent/callrecordfilter.md)
  Filters specified by the user to redial a call.
- [var callRecordToCallBack: INCallRecord?](./instartcallintent/callrecordtocallback.md)
  Details about a call to redial a missed call.
- [enum INCallAudioRoute](./incallaudioroute.md)
  Constants that describe the audio route for the call.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [UNNotificationContentProviding](../UserNotifications/unnotificationcontentproviding.md)

## See Also

### Starting a Call
- [protocol INStartCallIntentHandling](./instartcallintenthandling.md)
  An interface that handles requests to start audio and video calls.
- [class INStartCallIntentResponse](./instartcallintentresponse.md)
  Your app’s response to a start call intent.
- [enum INStartCallCallRecordToCallBackUnsupportedReason](./instartcallcallrecordtocallbackunsupportedreason.md)
  A reason why your app can’t use a record to call a person back.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent)*