# Apple Watch support

**Framework**: SiriKit  
**Role**: API Collection

Display relevant shortcuts on the Siri watch face.

**Availability**:
- watchOS 5.0+ - Deprecated in 11.0

#### Overview

An [`INRelevantShortcut`](https://developer.apple.com/documentation/intents/inrelevantshortcut) describes an action that might be useful or meaningful to the user within a particular context. For instance, a user might want to start a workout when they arrive at the gym, meditate in the morning, or find out about a new episode of their favorite TV show as soon it’s available. The system uses the shortcut’s relevance providers, as well as other signals, to determine when the shortcut is likely relevant to the user.

> ❗ **Important**: The Siri Watch Face is available in watchOS 11 and earlier. To make content available in the Smart Stack on Apple Watch using widgets, refer to [WidgetKit](../WidgetKit/WidgetKit.md), [Increasing the visibility of widgets in Smart Stacks](../WidgetKit/widget-suggestions-in-smart-stacks.md), and [App Intents](../AppIntents/AppIntents.md). For more information about migrating your SiriKit code to App Intents, refer to [Migrating widgets from SiriKit Intents to App Intents](../WidgetKit/migrating-from-sirikit-intents-to-app-intents.md) and [Soup Chef with App Intents: Migrating custom intents](./soup-chef-with-app-intents-migrating-custom-intents.md).

The Siri watch face updates throughout the day to offer shortcuts or glanceable information. For details on suggesting relevant shortcuts on the Siri watch face, see [Defining Relevant Shortcuts for the Siri Watch Face](./defining-relevant-shortcuts-for-the-siri-watch-face.md).

Users can collect multiple widgets into a Smart Stack. A Smart Stack rotates to widgets and suggests new widgets based on relevance cues. For details on using shortcuts to influence Smart Stacks, see [Increasing the visibility of widgets in Smart Stacks](../WidgetKit/widget-suggestions-in-smart-stacks.md).

## Topics

### Siri watch face
- [Displaying Shortcut Information in a Siri Watch Face Card](./displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [class INDefaultCardTemplate](https://developer.apple.com/documentation/intents/indefaultcardtemplate)
  A card template for customizing the Siri watch face for a shortcut.
- [Defining Relevant Shortcuts for the Siri Watch Face](./defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [class INRelevantShortcut](https://developer.apple.com/documentation/intents/inrelevantshortcut)
  An object that defines a shortcut and its relevance to the user.
- [class INRelevantShortcutStore](https://developer.apple.com/documentation/intents/inrelevantshortcutstore)
  An object that saves relevant shortcuts.
### Relevance Providers
- [class INRelevanceProvider](https://developer.apple.com/documentation/intents/inrelevanceprovider)
  An abstract class that represents a relevance provider.
- [class INDailyRoutineRelevanceProvider](https://developer.apple.com/documentation/intents/indailyroutinerelevanceprovider)
  The provider class that specifies a relevant daily routine.
- [class INDateRelevanceProvider](https://developer.apple.com/documentation/intents/indaterelevanceprovider)
  The provider class that specifies a relevant day and time.
- [class INLocationRelevanceProvider](https://developer.apple.com/documentation/intents/inlocationrelevanceprovider)
  The provider class that specifies a relevant location.

## See Also

### Shortcuts and Donations
- [Offering Actions in the Shortcuts App](./offering-actions-in-the-shortcuts-app.md)
  Suggest shortcuts users may want to add to Siri or combine with other actions in their own shortcuts.
- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](./adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Donating Shortcuts](./donating-shortcuts.md)
  Tell Siri about shortcuts to actions that the user performed in your app.
- [Deleting Donated Shortcuts](./deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Soup Chef: Accelerating App Interactions with Shortcuts](./soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
- [Soup Chef with App Intents: Migrating custom intents](./soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [Adding Shortcuts for Wind Down](./adding-shortcuts-for-wind-down.md)
  Reveal your app’s shortcuts inside the Health app.
- [class INShortcutReference](https://developer.apple.com/documentation/intents/inshortcutreference)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INInteraction](https://developer.apple.com/documentation/intents/ininteraction)
  An interaction between the user and your app involving an intent object.
- [enum INShortcut](https://developer.apple.com/documentation/intents/inshortcut-swift.enum)
  An action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INVoiceShortcutCenter](https://developer.apple.com/documentation/intents/invoiceshortcutcenter)
  Retrieve the user’s shortcuts and make shortcut suggestions.
- [class INVoiceShortcut](https://developer.apple.com/documentation/intents/invoiceshortcut)
  A shortcut the user added to Siri.
- [struct INShortcutAvailabilityOptions](https://developer.apple.com/documentation/intents/inshortcutavailabilityoptions)
  Defined contexts in which an intent or activity might be relevant to a user.
- [class INShortcutReference](https://developer.apple.com/documentation/intents/inshortcutreference)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INIntentDonationMetadata](https://developer.apple.com/documentation/intents/inintentdonationmetadata)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/watch-and-widget-support)*