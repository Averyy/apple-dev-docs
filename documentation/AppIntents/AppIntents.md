# App Intents

**Framework**: App Intents  
**Kind**: module

Make your app’s content and actions discoverable with system experiences like Spotlight, widgets, and the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Mentions

- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
- [Creating your first app intent](creating-your-first-app-intent.md)

#### Overview

The App Intents framework provides functionality to deeply integrate your app’s actions and content with system experiences across platforms, including Siri, Spotlight, widgets, controls and more. With Apple Intelligence and enhancements to App Intents, Siri will suggest your app’s actions to help people discover your app’s features and gains the ability to take actions in and across apps.

![A hero image of an App Intents framework icon.](https://docs-assets.developer.apple.com/published/4c11e7619eec4482c4c0d9fdb7676e38/app-intents-hero%402x.png)

By adopting the App Intents framework, you allow people to personalize their devices by instantly using your app’s functionality with:

- Interactions with Siri, including those that use the personal context awareness and action capabilities of Apple Intelligence.
- Spotlight suggestions and search.
- Actions and automations in the Shortcuts app.
- Hardware interactions that initiate app actions, like the Action button and squeeze gestures on Apple Pencil.
- Focus to allow people to reduce distractions.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, App Intents enables you to express your app’s actions, by offering an App Shortcut. People can then ask Siri to take those actions on their behalf, whether they’re in your app or elsewhere in the system. Use App Entities to expose content in your app to Spotlight and semantic indexing with Apple Intelligence. People can then ask Siri to retrieve information from your app, like asking Siri to pull up flight information from a travel app to share with a loved one.

You reuse these components with other technologies to offer additional features and experiences that make your app and its functionality even more discoverable and widely available. For example, you reuse modular App Intents code together with [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit) to offer:

- Interactive widgets
- Controls
- Live Activities

To learn more about features that the App Intents framework enables and how you can best adopt the framework, see [`Making actions and content discoverable and widely available`](making-actions-and-content-discoverable-and-widely-available.md).

For design guidance, see [`Human Interface Guidelines > App Shortcuts`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-shortcuts), [`Human Interface Guidelines > Siri`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/siri), and [`Human Interface Guidelines > Action Button`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/action-button).

## Topics

### Essentials
- [App Intents updates](../Updates/AppIntents.md)
  Learn about important changes in App Intents.
- [Making actions and content discoverable and widely available](making-actions-and-content-discoverable-and-widely-available.md)
  Adopt App Intents to make your app discoverable with Spotlight, controls, widgets, and the Action button.
- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [Adopting App Intents to support system experiences](adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts.
- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
### Siri and Apple Intelligence
- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
  Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence.
- [Making onscreen content available to Siri and Apple Intelligence](making-onscreen-content-available-to-siri-and-apple-intelligence.md)
  Enable Siri and Apple Intelligence to respond to a person’s questions and action requests for your app’s onscreen content.
- [App intent domains](app-intent-domains.md)
  Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.
- [Making your app’s functionality available to Siri](making-your-app-s-functionality-available-to-siri.md)
  Add assistant schemas to your app so Siri can complete requests, and integrate your app with Apple Intelligence, Spotlight, and other system experiences.
### Visual intelligence
- [Integrating your app with visual intelligence](../VisualIntelligence/integrating-your-app-with-visual-intelligence.md)
  Enable people to find app content that matches their surroundings or objects onscreen with visual intelligence.
- [Visual Intelligence](../VisualIntelligence/VisualIntelligence.md)
  Include your app’s content in search results that visual intelligence provides.
- [protocol IntentValueQuery](intentvaluequery.md)
  A query that provides entity values to the system; for example, for visual intelligence search.
### Interactive Snippets
- [Displaying static and interactive snippets](displaying-static-and-interactive-snippets.md)
  Enable people to view the outcome of an app intent and immediately perform follow-up actions.
- [protocol SnippetIntent](snippetintent.md)
  An app intent that presents an interactive snippet onscreen.
### Other system experiences
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Allow people to find your app’s content in Spotlight by donating app entities to its semantic index.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
- [Action button on iPhone and Apple Watch](actionbutton.md)
  Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.
- [Developing a WidgetKit strategy](../WidgetKit/Developing-a-WidgetKit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
### SiriKit migration
- [Soup Chef with App Intents: Migrating custom intents](../SiriKit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
### Actions
- [App intents](app-intents.md)
  Define the custom actions your app exposes to the system, and incorporate support for existing SiriKit intents.
- [Intent discovery](intent-discovery.md)
  Donate your app’s intents to the system to help it identify trends and predict future behaviors.
- [App Shortcuts](app-shortcuts.md)
  Integrate your app’s intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models.
### Parameters, custom data types, and queries
- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.
### Utility types
- [Common types](common-data-types.md)
  Specify common types that your app supports, including currencies, files, and contacts.
### Errors
- [struct AppIntentError](appintenterror.md)
  Errors that your intent-handling code can return to indicate problems while interpreting or executing an app intent.
### Protocols
- [protocol AppIntentSceneDelegate](appintentscenedelegate.md)
  Implement this protocol on your UIScene delegate to handle AppIntent invocations targeting a specific scene Example:
- [protocol AppShortcutsContent](appshortcutscontent.md)
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
- [protocol ShowsSnippetIntent](showssnippetintent.md)
  The result of performing an action that present a snippet generated by a `SnippetIntent`-conforming type.
- [protocol TargetContentProvidingIntent](targetcontentprovidingintent.md)
- [protocol UISceneAppIntent](uisceneappintent.md)
- [protocol UndoableIntent](undoableintent.md)
### Structures
- [struct ConfirmationConditions](confirmationconditions.md)
  Conditions for a confirmation request.
- [struct EntityPropertyModifiers](entitypropertymodifiers.md)
- [struct EntityURLRepresentation](entityurlrepresentation.md)
  The URL representation of an app entity.
- [struct EnumURLRepresentation](enumurlrepresentation.md)
  The URL representation of an app enum.
- [struct FileEntityIdentifier](fileentityidentifier.md)
  An identifier for an app entity that refers to a document or other file.
- [struct IntentChoiceOption](intentchoiceoption.md)
  A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.
- [struct IntentModes](intentmodes.md)
  A set of options that describe an app intent’s behavior.
- [struct IntentURLRepresentation](intenturlrepresentation.md)
  The URL representation of an app intent.
### Macros
- [macro UnionValue()](unionvalue().md)
### Enumerations
- [enum AppShortcutPhraseToken](appshortcutphrasetoken.md)
  Dynamic values you can include in the spoken phrases that run your shortcut.
- [enum VideoCategory](videocategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntents)*