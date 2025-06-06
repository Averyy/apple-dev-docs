# Offering Actions in the Shortcuts App

**Framework**: SiriKit

Suggest shortcuts users may want to add to Siri or combine with other actions in their own shortcuts.

#### Overview

When the user performs an action in your app, donate a shortcut that accelerates user access to the action. Siri shows these donated interactions to the user in places such as Spotlight search, Lock Screen, and the Siri watch face.

However, sometimes there are actions in your app the user hasn’t performed that might be of interest to them. For example, perhaps your soup-ordering app features a special soup every day. The user has never ordered the daily soup special, but they might be interested in the option to add a  shortcut to Siri. Your app can provide this option by making a shortcut suggestion.

> **Note**:  A donated interaction or suggested shortcut containing a system intent defines a specific action. The user can’t customize the parameters of such an action in the Shortcuts app. Instead, define a custom intent. For more information on defining custom intents, see [`Adding User Interactivity with Siri Shortcuts and the Shortcuts App`](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md).

 A donated interaction or suggested shortcut containing a system intent defines a specific action. The user can’t customize the parameters of such an action in the Shortcuts app. Instead, define a custom intent. For more information on defining custom intents, see [`Adding User Interactivity with Siri Shortcuts and the Shortcuts App`](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md).

##### Suggest a Shortcut

To suggest a shortcut to an action that the user hasn’t performed but may want to add to Siri, create an [`INShortcutReference`](https://developer.apple.com/documentation/intents/inshortcutreference) object with either an [`INIntent`](https://developer.apple.com/documentation/intents/inintent) or [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object that defines the action. Then add the shortcut to an array. Repeat for each suggestion your app wants to make. After creating the list of shortcut suggestions, call [`setShortcutSuggestions(_:)`](https://developer.apple.com/documentation/intents/invoiceshortcutcenter/setshortcutsuggestions(_:)), passing in the shortcuts.

```swift
import Intents

// Add a user activity to the list of suggestions.
var suggestions = [INShortcut(userActivity: orderFavoriteBeverageUserActivity)]

// Add an intent to the list of suggestions. To create
// a shortcut from an intent, the intent must be valid.
if let shortcut = INShortcut(intent: orderSoupOfTheDayIntent) {
    suggestions.append(shortcut)
}

// Suggest the shortcuts.
INVoiceShortcutCenter.shared.setShortcutSuggestions(suggestions)
```

##### Update Suggestions

Provide shortcut suggestions that represent actions that pertain to the user. This list may change over time for reasons such as:

- The addition or removal of features from your app.
- A change in the way the user interacts with your app.

To update the shortcut suggestion list, replace the existing list by calling [`setShortcutSuggestions(_:)`](https://developer.apple.com/documentation/intents/invoiceshortcutcenter/setshortcutsuggestions(_:)) and passing in a new list of suggestions. If you want to remove all suggestions made by your app, call the same method, passing in an empty array.

Changes to the list of shortcut suggestions don’t affect shortcuts the user adds to Siri. For instance, if the user adds the suggested  shortcut to Siri and the app removes the suggestion from the list some time later, that shortcut is still available to the user.

## See Also

- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Deleting Donated Shortcuts](deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Dispatching intents to handlers](dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving Siri Media Interactions and App Selection](improving-siri-media-interactions-and-app-selection.md)
  Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
- [Improving interactions between Siri and your messaging app](improving-interactions-between-siri-and-your-messaging-app.md)
  Donate app-specific content, use Siri’s contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
- [Registering Custom Vocabulary with SiriKit](registering-custom-vocabulary-with-sirikit.md)
  Register your app’s custom terminology, and provide sample phrases for how to use your app with Siri.
- [Confirming the Details of an Intent](confirming-the-details-of-an-intent.md)
  Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](handling-an-intent.md)
  Fulfill the intent and provide feedback to SiriKit about what you did.
- [Resolving the Parameters of an Intent](resolving-the-parameters-of-an-intent.md)
  Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Generating a List of Ride Options](generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [Handling the Ride-Booking Intents](handling-the-ride-booking-intents.md)
  Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Displaying Shortcut Information in a Siri Watch Face Card](displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/offering-actions-in-the-shortcuts-app)*