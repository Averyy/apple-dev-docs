# INPlayMediaIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intents handler’s response to a play media intent.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INPlayMediaIntentResponse
```

```objc
@interface INPlayMediaIntentResponse : INIntentResponse
```

## Overview

Create an instance of this class when you are:

- Confirming your app can play the media.
- Handling the request to play the media.

To send private state data from your Intents app extension to your app, store the data in an [`NSUserActivity`](../Foundation/nsuseractivity.md) object and include the object when creating the [`INPlayMediaIntentResponse`](./inplaymediaintentresponse.md) instance.

## Topics

### Creating a Play Media Intent Response
- [init(code: INPlayMediaIntentResponseCode, userActivity: NSUserActivity?)](./inplaymediaintentresponse/init%28code,useractivity%29.md)
  Creates a response for a play media intent.
### Providing the Response Code
- [var code: INPlayMediaIntentResponseCode](./inplaymediaintentresponse/code.md)
  A response code that indicates whether the app can play the media.
- [enum INPlayMediaIntentResponseCode](./inplaymediaintentresponsecode.md)
  Codes returned by an app or Intents app extension when handling or confirming a play media intent.
### Managing Now-Playing Information
- [var nowPlayingInfo: [String : Any]?](./inplaymediaintentresponse/nowplayinginfo.md)
  The now-playing information, such as title and artwork, for the media.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Playable Media Intents
- [protocol INPlayMediaIntentHandling](./inplaymediaintenthandling.md)
  The interface an object implements to confirm and handle play media intents.
- [class INPlayMediaIntent](./inplaymediaintent.md)
  An intent that contains information about media playable from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponse)*