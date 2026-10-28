# INInteraction

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An interaction between the user and your app involving an intent object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INInteraction
```

```objc
@interface INInteraction : NSObject
```

## Mentions

- [Configuring the View Controller for Your Custom Interface](../SiriKit/configuring-the-view-controller-for-your-custom-interface.md)
- [Donating Reservations](../SiriKit/donating-reservations.md)
- [Donating Shortcuts](../SiriKit/donating-shortcuts.md)
- [Improving Siri Media Interactions and App Selection](../SiriKit/improving-siri-media-interactions-and-app-selection.md)
- [Deleting Donated Shortcuts](../SiriKit/deleting-donated-shortcuts.md)
- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Overview

An [`INInteraction`](./ininteraction.md) object encapsulates information about a SiriKit request and your app’s response. SiriKit creates interaction objects automatically when it needs your app to respond to a specific intent, either by handling the intent or providing an error explaining why your app couldn’t handle the intent. SiriKit places the interaction in an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that the system passes to your app at launch time. You can also create instances of this class in your app and donate relevant interactions to the system.

Donating interactions provides contextual information that might be helpful to other apps. Some system apps use donated interactions to improve search results or to anticipate user actions. For example, a ride-booking app could donate an interaction containing the user’s planned ride information. If the user subsequently uses the Maps app to search for restaurants, Maps can show relevant results near the user’s destination.

You choose which of your app’s interactions you want to donate to the system. To donate an interaction, create an instance of this class, filling it with your intent object and response, and call the [`donate(completion:)`](./ininteraction/donate%28completion%29.md) method. You can also use the methods of this class to delete interactions when they are no longer relevant.

> **Note**:  Donate interactions only when the user initiates an interaction in your app. SiriKit already knows about interactions that it sends your app for intent handling.

## Topics

### Creating an Interaction Object
- [init(intent: INIntent, response: INIntentResponse?)](./ininteraction/init%28intent,response%29.md)
  Initializes and returns an interaction object with an intent object and your app’s response.
### Getting the Intent and Response
- [var intent: INIntent](./ininteraction/intent.md)
  The intent object that describes the user’s request.
- [var intentResponse: INIntentResponse?](./ininteraction/intentresponse.md)
  The response object that your app created in response to the request.
### Donating Interactions to the System
- [func donate(completion: (((any Error)?) -> Void)?)](./ininteraction/donate%28completion%29.md)
  Donates this interaction object to the system.
### Deleting Interactions from the System
- [class func deleteAll(completion: (((any Error)?) -> Void)?)](./ininteraction/deleteall%28completion%29.md)
  Deletes all interactions that you donated previously.
- [class func delete(with: [String], completion: (((any Error)?) -> Void)?)](./ininteraction/delete%28with,completion%29-2d1gs.md)
  Deletes the specified interactions that were donated by the calling app.
- [class func delete(with: String, completion: (((any Error)?) -> Void)?)](./ininteraction/delete%28with,completion%29-tcq9.md)
  Deletes the interactions with the specified group identifier.
### Accessing Interaction Attributes
- [var intentHandlingStatus: INIntentHandlingStatus](./ininteraction/intenthandlingstatus.md)
  The current state of the interaction.
- [var direction: INInteractionDirection](./ininteraction/direction.md)
  The direction in which information flowed to or from the device.
- [var dateInterval: DateInterval?](./ininteraction/dateinterval.md)
  The time at which the interaction started and its duration.
- [var identifier: String](./ininteraction/identifier.md)
  The unique identifier of the interaction.
- [var groupIdentifier: String?](./ininteraction/groupidentifier.md)
  The unique identifier of the interaction’s group.
### Getting the Value of a Parameter
- [func parameterValue(for: INParameter) -> Any?](./ininteraction/parametervalue%28for%29.md)
  Returns the value of the specified parameter of this interaction object.
### Constants
- [enum INIntentHandlingStatus](./inintenthandlingstatus.md)
  Constants indicating the current state of the interaction.
- [enum INInteractionDirection](./ininteractiondirection.md)
  Constants indicating whether the app is providing or receiving information.
### Initializers
- [init?(coder: NSCoder)](./ininteraction/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Shortcuts and Donations
- [Offering Actions in the Shortcuts App](../SiriKit/offering-actions-in-the-shortcuts-app.md)
  Suggest shortcuts users may want to add to Siri or combine with other actions in their own shortcuts.
- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](../SiriKit/adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Donating Shortcuts](../SiriKit/donating-shortcuts.md)
  Tell Siri about shortcuts to actions that the user performed in your app.
- [Deleting Donated Shortcuts](../SiriKit/deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Soup Chef: Accelerating App Interactions with Shortcuts](../SiriKit/soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
- [Soup Chef with App Intents: Migrating custom intents](../SiriKit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [Adding Shortcuts for Wind Down](../SiriKit/adding-shortcuts-for-wind-down.md)
  Reveal your app’s shortcuts inside the Health app.
- [class INShortcutReference](./inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
- [enum INShortcut](./inshortcut-swift.enum.md)
  An action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INVoiceShortcutCenter](./invoiceshortcutcenter.md)
  Retrieve the user’s shortcuts and make shortcut suggestions.
- [class INVoiceShortcut](./invoiceshortcut.md)
  A shortcut the user added to Siri.
- [struct INShortcutAvailabilityOptions](./inshortcutavailabilityoptions.md)
  Defined contexts in which an intent or activity might be relevant to a user.
- [class INShortcutReference](./inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INIntentDonationMetadata](./inintentdonationmetadata.md)
- [Apple Watch support](../SiriKit/watch-and-widget-support.md)
  Display relevant shortcuts on the Siri watch face.
- [Siri Event Suggestions](../SiriKit/siri-event-suggestions.md)
  Provide users with current, actionable information connected to a reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction)*