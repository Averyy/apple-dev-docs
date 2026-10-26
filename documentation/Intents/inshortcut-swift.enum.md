# INShortcut

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

An action available in your app that the system may suggest to a user or a user may add to Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 11.0+
- watchOS 5.0+

## Declaration

```swift
enum INShortcut
```

## Topics

### Creating a Shortcut
- [init?(intent: INIntent)](./inshortcut-swift.enum/init%28intent%29.md)
  Creates a shortcut with the specified intent.
- [init(userActivity: NSUserActivity)](./inshortcut-swift.enum/init%28useractivity%29.md)
  Creates a shortcut with the specified user activity.
### Getting the Intent
- [var intent: INIntent?](./inshortcut-swift.enum/intent.md)
  The intent that performs the action when invoking the shortcut.
### Getting the User Activity
- [var userActivity: NSUserActivity?](./inshortcut-swift.enum/useractivity.md)
  The user activity that defines the action to perform when invoking the shortcut.
### Using Reference Types
- [class INShortcutReference](./inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
### Enumeration Cases
- [INShortcut.intent(_:)](./inshortcut-swift.enum/intent%28_%29.md)
  The intent that performs the action when invoking the shortcut.
- [case userActivity(NSUserActivity)](./inshortcut-swift.enum/useractivity%28_%29.md)
  The user activity that defines the action to perform when invoking the shortcut.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [ReferenceConvertible](../Foundation/referenceconvertible.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcut-swift.enum)*