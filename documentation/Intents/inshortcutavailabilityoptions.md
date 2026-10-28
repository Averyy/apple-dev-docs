# INShortcutAvailabilityOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Defined contexts in which an intent or activity might be relevant to a user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct INShortcutAvailabilityOptions
```

```c
enum INShortcutAvailabilityOptions : NSUInteger;
```

## Overview

The system uses the set of availability options in a donated shortcut to provide the user with shortcuts relevant in a particular context or circumstance. For example, a meditation app could include an intent with [`sleepMindfulness`](./inshortcutavailabilityoptions/sleepmindfulness.md) in its [`shortcutAvailability`](../Foundation/nsuseractivity/shortcutavailability.md) options when calling [`setShortcutSuggestions(_:)`](./invoiceshortcutcenter/setshortcutsuggestions%28_%29.md). Then the Wind Down configuration screen in the Health app includes that intent in the Mindfulness category when guiding the user to set up shortcuts.

Provide accurate availability options when you suggest shortcuts to [`INVoiceShortcutCenter`](./invoiceshortcutcenter.md) with [`setShortcutSuggestions(_:)`](./invoiceshortcutcenter/setshortcutsuggestions%28_%29.md), and when you donate shortcuts based on user actions. If none of the options apply to an intent, provide an empty [`OptionSet`](../Swift/optionset.md).

> 💡 **Tip**:  Most shortcuts should specify a single activity type, but you can use an option set with more than one category if a shortcut really doesn’t fit neatly into a single category.

For more information on donating shortcuts effectively, see [Donating Shortcuts](../SiriKit/donating-shortcuts.md).

## Topics

### Providing Contexts
- [static var sleepMindfulness: INShortcutAvailabilityOptions](./inshortcutavailabilityoptions/sleepmindfulness.md)
  Meditation and other activities intended to facilitate mindfulness.
- [static var sleepJournaling: INShortcutAvailabilityOptions](./inshortcutavailabilityoptions/sleepjournaling.md)
  Writing and other daily logging activities.
- [static var sleepMusic: INShortcutAvailabilityOptions](./inshortcutavailabilityoptions/sleepmusic.md)
  Music suitable for falling asleep.
- [static var sleepPodcasts: INShortcutAvailabilityOptions](./inshortcutavailabilityoptions/sleeppodcasts.md)
  A podcast or other spoken audio.
- [static var sleepReading: INShortcutAvailabilityOptions](./inshortcutavailabilityoptions/sleepreading.md)
  A book or other reading material.
- [static var sleepWrapUpYourDay: INShortcutAvailabilityOptions](./inshortcutavailabilityoptions/sleepwrapupyourday.md)
  An activity in preparation for sleep such as personal grooming or reviewing the next day’s agenda.
- [static var sleepYogaAndStretching: INShortcutAvailabilityOptions](./inshortcutavailabilityoptions/sleepyogaandstretching.md)
  Physical activity to prepare for sleep.
### Creating an Availability Set
- [init(rawValue: UInt)](./inshortcutavailabilityoptions/init%28rawvalue%29.md)
  Returns the set of availability categories represented by the given value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

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
- [class INVoiceShortcut](./invoiceshortcut.md)
  A shortcut the user added to Siri.
- [class INShortcutReference](./inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INIntentDonationMetadata](./inintentdonationmetadata.md)
- [Apple Watch support](../SiriKit/watch-and-widget-support.md)
  Display relevant shortcuts on the Siri watch face.
- [Siri Event Suggestions](../SiriKit/siri-event-suggestions.md)
  Provide users with current, actionable information connected to a reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inshortcutavailabilityoptions)*