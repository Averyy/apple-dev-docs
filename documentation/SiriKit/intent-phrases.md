# Intent Phrases

**Framework**: SiriKit

The keys that you include in your global vocabulary file to show how users engage your app from Siri.

#### Overview

The `IntentPhrases` key contains sample phrases that a user might speak to initiate the handling of one of your intents. The value of this key is an array of dictionaries, each of which defines one of the sample phrases to speak. Each dictionary contains the following keys:

> ❗ **Important**:  Apps are expected to provide some example phrases. Siri displays your app’s sample phrases in Siri Guide so that users can access them directly from the Siri interface.

Xcode helps you add example phrases to your vocabulary file. When you create a property list file with the name `AppIntentVocabulary.plist`, Xcode knows that the file should contain custom vocabulary, and it makes only the relevant keys available in the property list editor. The figure below shows an example of a global vocabulary file in Xcode that contains sample phrases for starting a workout.

![Editing the sample phrases in Xcode](https://docs-assets.developer.apple.com/published/303fae81fa5dd2c525b5d0ecd208314c/media-2910039%402x.png)

## See Also

- [Parameter Vocabularies](parameter-vocabularies.md)
  The keys you include in your global vocabulary file to describe app-specific terms.
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
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.
- [Localizing Your Vocabulary for Chinese Dialects](localizing-your-vocabulary-for-chinese-dialects.md)
  Apply emphasis markers to your pronunciation tips to assist Siri with Chinese dialects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/intent-phrases)*