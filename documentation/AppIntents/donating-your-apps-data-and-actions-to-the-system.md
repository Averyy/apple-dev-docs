# Donating your app’s data and actions to the system

**Framework**: App Intents

Improve how people interact with your app through Apple Intelligence and Siri by teaching the system about your app’s data and actions.

#### Overview

Apple Intelligence and Siri help people perform actions and access that information outside your app. However, these features still rely on your app to provide content using the App Intents framework. Integrate this framework into your project and use it to define *app intents* for your app’s actions and *app entities* for your app’s data.

After you define app intents and app entities for your content, use *donations* to teach the system about those items at runtime. Donations help the system learn a person’s behaviors and find relevant information. When someone interacts with your app, donate app intents for any actions they perform. When you index your app’s content, include entities in your Spotlight search index so that search results can use them to launch your app. In your interface, assign entities to select views to reflect the data they contain. Apple Intelligence and Siri use this contextual information to improve interactions. For example, Siri can use the entities in your app’s interface to determine what someone means when they say “Send *this* message.”

For more on how to implement app intents, see [`Creating your first app intent`](creating-your-first-app-intent.md). For more on how to implement app entities, see [`Defining app entities for your custom data types`](defining-app-entities-for-your-custom-data-types.md).

##### Add App Entities to Your Spotlight Search Index

Apps use Spotlight to build a searchable index of their content, and the Core Spotlight framework offers APIs to index entities directly or add them to your existing Spotlight metadata. When a search yields a result with an app entity, Spotlight can use the entity to launch your app and navigate to the result. When building app intents to perform actions, Apple Intelligence and Siri can also use your entities to fill in parameters automatically.

Adding entities to your search index requires some changes to your app entity types. For details about how to make these changes, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

##### Help the System Predict Someones Future Actions

The system can suggest potential actions from the Lock Screen, in Siri Suggestions, and in other system interfaces. It makes these suggestions with the help of donations from your app and donations from system apps and features. For example, the system automatically donates the app intents that Siri, system apps, and other system features run. When you make donations from your app, you give the system a more complete picture of a person’s behaviors, which leads to more accurate suggestions.

Any time someone interacts with your app’s interface, donate app intents for the actions they perform. To make the donation, call one of the [`donate()`](appintent/donate()-1e60c.md) methods of your app intent, or use the shared [`IntentDonationManager`](intentdonationmanager.md) type. Both approaches deliver the app intent and an optional result to the system, which records the information for later use. The system doesn’t run the app intents you provide, but it can use them to construct similar app intents later.

For each app intent you donate:

- Fill in as much information as you can.
- Make sure every app intent has a title and description.
- Fill in as many other parameters and variables as makes sense. For example, when donating a Send Message app intent, include the recipients of the message but omit the message contents. The system uses such a donation to predict future recipients of messages, but not the future content of messages.

The system uses the contents of your app intents to craft a suitable message when suggesting an action. Typically, the system uses the intent’s title and parameter information to create this message, but you can provide custom messages by using the [`PredictableIntent`](predictableintent.md) protocol. Use this protocol to specify messages that contain custom text and optionally incorporate parameter values from the app intent. You can configure multiple messages with different parameters, and tailor each message to match the data present in the app intent.

> **Note**: Apps still need to donate Handoff-related actions using the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) type. For more information on how to add Handoff support to your app, see [`Implementing Handoff in Your App`](https://developer.apple.com/documentation/foundation/implementing-handoff-in-your-app).

##### Provide Contextual Awareness of Whats in Your Apps Interface

The views in your app’s interface reflect your app’s data — specifically, the portions of that data currently visible to someone. During a conversation, your app’s data offers additional context to help Apple Intelligence and Siri determine what someone meant. For example, when someone asks Siri to “Send *this* message”, Siri needs to knows what “this message” means. You provide Siri with this understanding by attaching app entities to your app’s views, and using them to reflect the data currently in your app’s interface.

When you configure your app’s interface, you fetch specific data objects and use them to configure the views you’re about to show. During this process, fetch the matching app entities and attach them to your views as well. If you use a set of views to show content from a single data object, you might attach the entity only to the top-level view. However, if you display a table or collection view, you might associate entities with each row or cell. Make sure the entities you attach to your interface accurately reflect the content you display. To assign entities to your views, use one of the following techniques:

- In SwiftUI, assign the identifier of your app entity to a view using the [`appEntityIdentifier(_:)`](https://developer.apple.com/documentation/swiftui/view/appentityidentifier(_:)) modifier.
- In UIKit or AppKit, assign the identifier of your app entity to the [`appEntityIdentifier`](appentityannotatable/appentityidentifier.md) property of a view or responder object.

For more information, see [`Providing contextual cues to Apple Intelligence and Siri`](providing-contextual-cues-to-apple-intelligence-and-siri.md).

##### Suggest Relevant Actions and Data From Your App

In specific situations, you might want to suggest app intents or app entities that you think someone might find relevant. The App Intents framework provides the following APIs to support these types of donations:

- Donate relevant actions to include in Smart Stacks on Apple Watch using the [`RelevantIntentManager`](relevantintentmanager.md) type.
- Donate relevant media items using the [`updateEntities(_:for:)`](relevantentities/updateentities(_:for:).md) method of [`RelevantEntities`](relevantentities.md).

When you donate actions using the `RelevantIntentManager` type, you provide both an action and the conditions for which that action applies. When the matching conditions occur, the system displays your action as a suggestion on someone’s Apple Watch. For example, a sports app might suggest someone start watching a match that involves their favorite team. You can suggest actions based on a specific time, location, or other conditions.

An app that manages media can use the [`RelevantEntities`](relevantentities.md) type to suggest relevant media items using app-specific criteria. As you collect contextual information about a person’s media usage, you can suggest media you think they might like. For example, you might use someone’s past music preferences to suggest a new band or album. The system offers your suggestions in relevant system interfaces.

## See Also

- [Making actions and content discoverable by Apple Intelligence](making-actions-and-content-discoverable-by-apple-intelligence.md)
  Equip the system so that Siri can work with your app by adding specific schemas from relevant domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/donating-your-apps-data-and-actions-to-the-system)*