# Intents

**Framework**: Intents  
**Kind**: module  
**Role**: Framework

Empower people to customize interactions for your app on their device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 12.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

#### Overview

> **Note**: SiriKit, Intents, and IntentsUI frameworks continue to provide legacy support for Shortcuts actions, widget configuration, and most existing Siri interactions. To implement modern support for these features and integrate your app with Apple Intelligence and Siri AI, use the [App Intents](../AppIntents/AppIntents.md) framework.

Intents is a [SiriKit](../SiriKit/SiriKit.md) framework you use to support interactions with Siri, Shortcuts, and widgets. Define custom intents for specific actions that someone can trigger with Siri or Shortcuts, and donate intents to help Siri learn someone’s habits and suggest relevant shortcuts over time. You can also provide shortcut suggestions that appear in the Shortcuts app or in Siri’s recommendations to help boost discoverability.

## Topics

### Intents
- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Resolving and Handling Intents](../SiriKit/resolving-and-handling-intents.md)
  Resolve, confirm, and handle user requests for your app’s services.
- [class INIntent](./inintent.md)
  A request to fulfill in your app or Intents extension.
- [class INIntentResponse](./inintentresponse.md)
  Your response to an intent object.
- [Intent Handling Infrastructure](../SiriKit/intent-handling-infrastructure.md)
  Specify required permissions and provide handlers for the intents your app supports, and configure app extensions.
- [Providing Hands-Free App Control with Intents](../SiriKit/providing-hands-free-app-control-with-intents.md)
  Resolve, confirm, and handle intents without an extension.
- [Resolution Results](../SiriKit/resolution-results.md)
  Resolve common types of data like strings and dates into specific values that your app recognizes.
- [Common Data Types](../SiriKit/common-data-types.md)
  Manage common data types such as strings, dates, currencies, images, and contacts.
### Standard Intents
- [Car Commands](../SiriKit/car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Lists and Notes](../SiriKit/lists-and-notes.md)
  Create and manage notes and to-do list items.
- [Media](../SiriKit/media.md)
  Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.
- [Messaging](../SiriKit/messaging.md)
  Send messages and search the user’s received messages.
- [Payments](../SiriKit/payments.md)
  Send payments between users or pay bills.
- [Restaurant Reservations](../SiriKit/restaurant-reservations.md)
  Create and manage restaurant reservations with help from the Maps app.
- [Ride Booking](../SiriKit/ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](../SiriKit/voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](../SiriKit/workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](../SiriKit/intent-class-identifiers.md)
  Identify intents that user notifications specify.
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
- [class INInteraction](./ininteraction.md)
  An interaction between the user and your app involving an intent object.
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
### Vocabulary
- [Registering Custom Vocabulary with SiriKit](../SiriKit/registering-custom-vocabulary-with-sirikit.md)
  Register your app’s custom terminology, and provide sample phrases for how to use your app with Siri.
- [class INVocabulary](./invocabulary.md)
  An object for registering user-specific vocabulary that Siri requests might include.
### Deprecated Symbols
- [Deprecated Symbols](../SiriKit/deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Macros
- [Macros](../SiriKit/macros.md)
### Classes
- [class INParameter](./inparameter.md)
  A parameter of an interaction object.
### Protocols
- [protocol INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
### Variables
- [INCarChargingConnectorTypeNACSAC](./incar/chargingconnectortype/nacsac.md)
- [INCarChargingConnectorTypeNACSDC](./incar/chargingconnectortype/nacsdc.md)
### Enumerations
- [INStickerType](./insticker/stickertype.md)

## See Also

### Frameworks
- [IntentsUI](../IntentsUI/IntentsUI.md)
  Customize content in the interface for Siri and Maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents)*