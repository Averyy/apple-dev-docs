# INVoiceShortcut

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A shortcut the user added to Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INVoiceShortcut
```

```objc
@interface INVoiceShortcut : NSObject
```

#### Overview

To add a shortcut to Siri, create an [`INShortcutReference`](./inshortcutreference.md) object and add it using [`INUIAddVoiceShortcutViewController`](../IntentsUI/inuiaddvoiceshortcutviewcontroller.md). You don’t create an instance of [`INVoiceShortcut`](./invoiceshortcut.md); the system creates the instance for you when an instance is needed.

## Topics

### Accessing Shortcut Information
- [var identifier: UUID](./invoiceshortcut/identifier.md)
  The unique identifier for the shortcut.
- [var invocationPhrase: String](./invoiceshortcut/invocationphrase.md)
  The phrase the user speaks to invoke the shortcut.
- [var shortcut: INShortcut](./invoiceshortcut/shortcut.md)
  The shortcut Siri invokes when the user speaks the invocation phrase.
### Initializers
- [init?(coder: NSCoder)](./invoiceshortcut/init%28coder%29.md)

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
- [class INInteraction](./ininteraction.md)
  An interaction between the user and your app involving an intent object.
- [enum INShortcut](./inshortcut-swift.enum.md)
  An action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INVoiceShortcutCenter](./invoiceshortcutcenter.md)
  Retrieve the user’s shortcuts and make shortcut suggestions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcut)*