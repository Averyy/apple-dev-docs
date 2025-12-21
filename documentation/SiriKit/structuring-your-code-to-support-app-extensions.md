# Structuring Your Code to Support App Extensions

**Framework**: SiriKit

Move your back-end services to a private framework so your app and app extensions can use them.

#### Overview

An app extension is an agent that acts on behalf of your app, vending services or providing information to the system when asked. Because they extend your app’s behavior, app extensions often need access to the same back-end services and data that your app uses.

Lightweight extensions that don’t include most of your app’s code can respond to a user’s request more quickly. Long-running tasks like playing music or tracking a workout need to happen in your app. If necessary, you can resolve the parameters of an intent in an extension, then instruct SiriKit to launch your app for the final handling step.

If your app and app extension share services, consider structuring your code in the following way:

-  A private shared framework lets you place the code for accessing your services in one code module and use that code from multiple targets. Shared frameworks minimize the size of both executables and make testing easier by ensuring that each executable uses the same code path.
-  Put relevant images and data files into a shared container so your app and app extension can use them. You enable shared container support in the Capabilities tab of each target.

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
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.
- [Intent Phrases](intent-phrases.md)
  The keys that you include in your global vocabulary file to show how users engage your app from Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/structuring-your-code-to-support-app-extensions)*