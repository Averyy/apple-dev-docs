# Apple Intelligence and Siri AI

**Framework**: App Intents

Integrate your app with Apple Intelligence and bring it to Siri AI.

#### Overview

Apple Intelligence combines language models with your app’s actions and content to power Siri AI. It uses the app intents, app entities, and app enums you define to wrap your app’s actions and content in types the system can understand. Perform the following additional steps to make actions and content discoverable by Apple Intelligence and Siri AI:

**Index entities to make them available in Spotlight.** Apple Intelligence uses the semantic search capabilities of Spotlight to find your app’s content, even when someone describes it vaguely.

**Choose transferable types.** Conforming your [`AppEntity`](appentity.md) to [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) or types from the App Intents framework enables the system to move content across apps so people can perform tasks across apps with Siri AI.

**Adopt schemas.** Schemas define the structure of your app intents, app entities, and app enums. Schemas act as a contract between your app and the system; Apple Intelligence uses them to identify, query, and understand actions and content. Siri AI uses the schemas to match actions and content to phrases people say in everyday conversation.

**Associate entities with views and other structures.** People use Siri AI to interact with content that’s visible onscreen, but that content is private to your app. Associating views, user activities, or other visible content with app entities gives Apple Intelligence onscreen context. For example, onscreen context lets someone refer to an onscreen photo conversationally as “this photo”.

**Donate actions and content.** Donations give Apple Intelligence behavioral cues to identify trends, predict future behavior, and disambiguate vague requests. For example, if someone asks your app for the weather each morning, Apple Intelligence can proactively suggest the same action.

## Topics

### Content
- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Update your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.
### Onscreen context
- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)
  Annotate your interface with app entities to offer contextual information about your app’s onscreen content.
- [App schema domains](app-schema-domains.md)
  Declare support for well-known actions and content by applying system-defined schemas to your app intents, app entities, and app enumerations.
- [protocol UITableViewAppIntentsDataSource](uitableviewappintentsdatasource.md)
  The methods that an object adopts to make items in a table view discoverable by Apple Intelligence and Siri.
- [protocol NSTableViewAppIntentsDataSource](nstableviewappintentsdatasource.md)
  The methods that an object adopts to make items in a table view or outline view discoverable by Apple Intelligence and Siri.
- [protocol UICollectionViewAppIntentsDataSource](uicollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.
- [protocol NSCollectionViewAppIntentsDataSource](nscollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.
### Actions
- [Making actions and content discoverable by Apple Intelligence](making-actions-and-content-discoverable-by-apple-intelligence.md)
  Equip the system so that Siri can work with your app by adding specific schemas from relevant domains.
- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)
  Improve how people interact with your app through Apple Intelligence and Siri by teaching the system about your app’s data and actions.
### Sample code
- [Integrating your messaging app with Apple Intelligence](integrating-your-messaging-app-with-apple-intelligence.md)
  Adopt message schemas so people can send messages and manage conversations with Siri.
- [Integrating your calendar app with Apple Intelligence](integrating-your-calendar-app-with-apple-intelligence.md)
  Adopt calendar schemas so people can create, find, and manage events with Siri.
- [Integrating your music app with Apple Intelligence](integrating-your-music-app-with-apple-intelligence.md)
  Adopt the audio and clock schemas so people can play music and set alarms with Siri.
- [Integrating your photo app with Apple Intelligence](integrating-your-photo-app-with-apple-intelligence.md)
  Adopt photo schemas so people can edit and manage photos with Siri.

## See Also

- [Adopting App Intents to support system experiences](adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities so people can use your app’s content and actions across system experiences.
- [Spotlight integration](spotlight.md)
  Add your entities to your app’s Spotlight index, and automate the indexing of your content.
- [App Shortcuts](app-shortcuts.md)
  Improve the experience of using your app intents and entities in system experiences like Siri, Spotlight, and the Shortcuts app.
- [Widgets, Live Activities, and Controls](widgets-live-activities-and-controls.md)
  Implement interactive widgets, controls, watch complications, and Live Activities using app intents.
- [Hardware interactions](hardware-interactions.md)
  Run your App Shortcuts from the Action button on iPhone or Apple Watch, or launch your own conversational app from the side button on iPhone.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
- [Visual intelligence](visual-intelligence.md)
  Match images to your app’s content and report the results to the Visual Intelligence framework using an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai)*