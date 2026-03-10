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

- [Creating your first app intent](creating-your-first-app-intent.md)
- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)

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
### System experiences
- [Adopting App Intents to support system experiences](adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts.
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Annotate your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.
- [Launching your voice-based conversational app from the side button of iPhone](launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md)
  Let people in Japan configure the side button of iPhone to launch your voice-based conversational app.
- [Siri](siri.md)
  Let people complete tasks with voice commands, search, and other system experiences by integrating your app with Siri and Apple Intelligence.
- [Visual intelligence](visual-intelligence.md)
  Integrate your app with visual intelligence and include your content in its search results.
- [App Shortcuts](app-shortcuts.md)
  Integrate your app’s intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models.
- [Widgets, Live Activities, and controls](widgets-and-live-activities.md)
  Use app intents make your widgets and Live Activities interactive, offer controls, and suggest widgets in Smart Stacks.
- [Action button on iPhone and Apple Watch](actionbutton.md)
  Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
### Actions
- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [App intents](app-intents.md)
  Define the custom actions your app exposes to the system using specialized intents.
- [App intent domains](app-intent-domains.md)
  Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.
- [Intent infrastructure](intent-infrastructure.md)
  Provide supplemental context for your intents, and create infrastructure to make app intents reusable across your apps.
### Parameters and data types
- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.
- [Common data types](common-data-types.md)
  Specify common types that your app supports, including currencies, files, and contacts.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Static parameter types](app-enums.md)
  Types that represent an enumerable list of static parameter values.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.
### Outcomes
- [Displaying static and interactive snippets](displaying-static-and-interactive-snippets.md)
  Enable people to view the outcome of an app intent and immediately perform follow-up actions.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [protocol IntentResult](intentresult.md)
  A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.
- [struct IntentResultContainer](intentresultcontainer.md)
  An object that represents the output of a completed intent.
- [protocol OpensIntent](opensintent.md)
  The result of performing an action that delivers an app intent back to the initiator of the action.
- [protocol ProvidesDialog](providesdialog.md)
  The result of performing an action that delivers a dialog back to the initiator of the action.
- [protocol ReturnsValue](returnsvalue.md)
  The result of performing an action that delivers a value back to the initiator.
- [protocol ShowsSnippetIntent](showssnippetintent.md)
  The result of performing an action that present a snippet generated by a `SnippetIntent`-conforming type.
- [protocol ShowsSnippetView](showssnippetview.md)
  The result of performing an action that delivers a view back to the initiator of the action.
- [protocol ResultsCollection](resultscollection.md)
  A protocol representing a collection of returned items with support for sectioning.
### Choices and confirmation
- [struct IntentChoiceOption](intentchoiceoption.md)
  A structure representing an entry in a list of options for a person to choose from before an app intent resumes its action.
- [struct ConfirmationConditions](confirmationconditions.md)
  Conditions for a confirmation request.
### Navigation and app launch
- [protocol AppIntentSceneDelegate](appintentscenedelegate.md)
  Implement this protocol on your UIScene delegate to handle AppIntent invocations targeting a specific scene Example:
- [struct IntentModes](intentmodes.md)
  A set of options that describe an app intent’s behavior.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
### SiriKit migration
- [Soup Chef with App Intents: Migrating custom intents](../SiriKit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [protocol CustomIntentMigratedAppIntent](customintentmigratedappintent.md)
  An interface for replacing a custom SiriKit intent that allows existing shortcuts and donations to continue working.
### Errors
- [struct AppIntentError](appintenterror.md)
  Errors that your intent-handling code can return to indicate problems while interpreting or executing an app intent.
### Protocols
- [protocol UndoableIntent](undoableintent.md)
### Enumerations
- [enum VideoCategory](videocategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntents)*