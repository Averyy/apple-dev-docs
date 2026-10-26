# INVoiceShortcutCenter

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Retrieve the user’s shortcuts and make shortcut suggestions.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INVoiceShortcutCenter
```

```objc
@interface INVoiceShortcutCenter : NSObject
```

#### Overview

With Shortcut Center, your app can:

- Retrieve shortcuts associated with your app that the user added to Siri.
- Suggest shortcuts the user may want to add to Siri.

Before you can retrieve or suggest shortcuts, get a reference to the Shortcut Center from the [`shared`](./invoiceshortcutcenter/shared.md) class property.

To retrieve all shortcuts associated with your app, call [`getAllVoiceShortcuts(completion:)`](./invoiceshortcutcenter/getallvoiceshortcuts%28completion%29.md). To retrieve a particular shortcut, use the [`getVoiceShortcut(with:completion:)`](./invoiceshortcutcenter/getvoiceshortcut%28with,completion%29.md) method, passing in the shortcut’s identifier. These methods return shortcuts associated with your app that the user added to Siri using your app or the Settings app.

To suggest shortcuts for actions that the user hasn’t performed in your app but may want to add to Siri, call [`setShortcutSuggestions(_:)`](./invoiceshortcutcenter/setshortcutsuggestions%28_%29.md), passing in a list of suggested shortcuts. The user views the suggestions in the Gallery of the Shortcuts app. For more information, see [Offering Actions in the Shortcuts App](../SiriKit/offering-actions-in-the-shortcuts-app.md).

## Topics

### Getting the Shortcut Center
- [class var shared: INVoiceShortcutCenter](./invoiceshortcutcenter/shared.md)
  The shared shortcut center.
### Getting Shortcuts Added to Siri
- [func getAllVoiceShortcuts(completion: ([INVoiceShortcut]?, (any Error)?) -> Void)](./invoiceshortcutcenter/getallvoiceshortcuts%28completion%29.md)
  Retrieves all shortcuts added to Siri for your app.
- [func getVoiceShortcut(with: UUID, completion: (INVoiceShortcut?, (any Error)?) -> Void)](./invoiceshortcutcenter/getvoiceshortcut%28with,completion%29.md)
  Retrieves a shortcut the user added to Siri.
### Setting Suggested Shortcuts
- [func setShortcutSuggestions([INShortcut])](./invoiceshortcutcenter/setshortcutsuggestions%28_%29.md)
  Suggests shortcuts the user may want to add to Siri.
- [class INShortcutReference](./inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcutcenter)*