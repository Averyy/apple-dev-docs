# SiriKit

**Framework**: SiriKit

Empower users to interact with their devices through voice, intelligent suggestions, and personalized workflows.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 12.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

#### Overview

The Intents and IntentsUI frameworks drive interactions that start with “Hey Siri…”, Shortcuts actions, and widget configuration. The system also incorporates intents and user activities your app donates into contextual suggestions in Maps, Calendar, Watch complications, widgets, and search results.

![A collection of devices, including a MacBook Air, an iPhone, an Apple Watch, and a HomePod mini. The devices display user interactions that SiriKit enables. On the MacBook Air, the Shortcuts app is open with a collection of shortcuts in the All Shortcuts section. The iPhone displays a Siri Suggestion with the Maps icon. The Apple Watch displays the Siri animation and the words “What can I help you with?”](https://docs-assets.developer.apple.com/published/06419e94cd4dfe4473c92e9964f7377f/media-3849683%402x.png)

Use the standard intents that the system provides to empower actions users already ask Siri to do, such as playing music or sending a text message. You can also offer your app’s unique capabilities throughout the system by designing custom intents. For more details about defining custom intents, see [`Adding User Interactivity with Siri Shortcuts and the Shortcuts App`](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md).

You can process intents directly in your app, or in an Intents app extension. For guidance on setting up an app extension and sharing information between your app and extension, see [`Structuring Your Code to Support App Extensions`](structuring-your-code-to-support-app-extensions.md).

To display branding or other customized content in Siri and Maps after you fulfill a user request, create a custom view controller in an IntentsUI app extension. See [`Creating an Intents UI Extension`](creating-an-intents-ui-extension.md) for more details.

> ❗ **Important**:  With a person’s permission, an installed health research app that uses [`SensorKit`](https://developer.apple.com/documentation/SensorKit) entitlements may collect Face Metrics data while your SiriKit app is in use. To prevent SensorKit from collecting Face Metrics data while your app is in use, you can set the [`SRResearchDataGeneration`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration) information property list key to `NO`.

## Topics

### Frameworks
- [Intents](../intents/intents.md)
  Empower people to customize interactions for your app on their device.
- [IntentsUI](../intentsui/intentsui.md)
  Customize content in the interface for Siri and Maps.
### Sample code
- [Adding Shortcuts for Wind Down](adding-shortcuts-for-wind-down.md)
  Reveal your app’s shortcuts inside the Health app.
- [Booking Rides with SiriKit](booking-rides-with-sirikit.md)
  Add Intents extensions to your app to handle requests to book rides using Siri and Maps.
- [Handling Payment Requests with SiriKit](handling-payment-requests-with-sirikit.md)
  Add an Intent Extension to your app to handle money transfer requests with Siri.
- [Handling Workout Requests with SiriKit](handling-workout-requests-with-sirikit.md)
  Add an Intent Extension to your app that handles requests to control workouts with Siri.
- [Integrating Your App with Siri Event Suggestions](integrating-your-app-with-siri-event-suggestions.md)
  Donate reservations and provide quick access to event details throughout the system.
- [Managing Audio with SiriKit](managing-audio-with-sirikit.md)
  Control audio playback and handle requests to add media using SiriKit Media Intents.
- [Providing Hands-Free App Control with Intents](providing-hands-free-app-control-with-intents.md)
  Resolve, confirm, and handle intents without an extension.
- [Soup Chef: Accelerating App Interactions with Shortcuts](soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
- [Soup Chef with App Intents: Migrating custom intents](soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
### Articles
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
- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.
- [Intent Phrases](intent-phrases.md)
  The keys that you include in your global vocabulary file to show how users engage your app from Siri.
- [Localizing Your Vocabulary for Chinese Dialects](localizing-your-vocabulary-for-chinese-dialects.md)
  Apply emphasis markers to your pronunciation tips to assist Siri with Chinese dialects.
- [Parameter Vocabularies](parameter-vocabularies.md)
  The keys you include in your global vocabulary file to describe app-specific terms.
- [Offering Actions in the Shortcuts App](offering-actions-in-the-shortcuts-app.md)
  Suggest shortcuts users may want to add to Siri or combine with other actions in their own shortcuts.
- [Creating an Intents App Extension](creating-an-intents-app-extension.md)
  Add and configure an Intents app extension in your Xcode project.
- [Requesting Authorization to Use Siri](requesting-authorization-to-use-siri.md)
  Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.
- [Structuring Your Code to Support App Extensions](structuring-your-code-to-support-app-extensions.md)
  Move your back-end services to a private framework so your app and app extensions can use them.
- [Providing Live Status Updates](providing-live-status-updates.md)
  Provide regular updates to Maps about the status of a booked ride.
- [Donating Shortcuts](donating-shortcuts.md)
  Tell Siri about shortcuts to actions that the user performed in your app.
- [Configuring the View Controller for Your Custom Interface](configuring-the-view-controller-for-your-custom-interface.md)
  Configure your view controller to replace or augment the default interface in Siri or Maps.
- [Configuring Your Intents UI App Extension Target](configuring-your-intents-ui-app-extension-target.md)
  Configure your Xcode project to include an Intents UI app extension that you use to customize the Siri and Maps interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SiriKit)*