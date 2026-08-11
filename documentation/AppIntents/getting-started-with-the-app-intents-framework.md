# Getting started with the App Intents framework

**Framework**: App Intents

Make your app’s actions and content available to the rest of the system using the App Intents framework.

#### Overview

People use apps to view and interact with their content, but they can also interact with that content in other ways. Someone might use Siri while driving to perform actions using your app, like sending a message or creating a note. When Spotlight displays your content in search results, the person can tap that result to launch your app to display the content there. Widgets can display your content from the Home Screen, Lock Screen and other places, and even let people interact with that content. All of these features rely your app supporting the App Intents framework, which provides the infrastructure to make your content available from outside your app. Make the adoption of this framework a core feature of every app you create.

![An illustration that shows how intents represent actions and entities represent content that an app makes available to Apple Intelligence to enable system experiences like Siri, Spotlight, or Shortcuts.](https://docs-assets.developer.apple.com/published/ab7f47190ba6e04fa129bfb72cb642b8/getting-started-with-the-app-intents-framework%402x.png)

With the App Intents framework, your code remains the source of truth and you use the framework’s protocols and other types to make your content available to the system. You can integrate support for app intents into your existing types or create entirely separate types. You decide which of your app’s actions and data types you want to make available, and typically focus on types that people recognize. For example, a travel app might expose data objects for travel destinations and actions to display or navigate to a specific destination.

##### Express Your Apps Actions Using App Intents

When someone interacts with your app’s interface, your app responds by performing an action. In a fitness app, someone can start or stop a workout. In an email or messaging app, someone can edit and send messages. In a web browser, someone can view the page at a specific URL, create or close tabs, or create a bookmark to the current page. An *app intent* defines one of your app’s actions and the data you require to perform that action, and the system uses the app intents you create as the gateway to your app’s features.

As you design your app, identify actions that people might want to perform from outside your app. For each action, define an app intent type, then add parameters and variables for any data you need to perform the action. Make sure each app intent performs a unique action within your app, and use its parameters to configure it for different types of data. For example, instead of creating one app intent to play songs and a separate app intent to play albums, create a single app intent to play music and use a parameter to specify which song or album to play.

You can define custom app intents for any actions that are unique to your app, but build app intents for common actions from the built-in [`App schema domains`](app-schema-domains.md) whenever possible. The App Intents framework offers predefined app intents for actions that are common to multiple apps. For example, you might use these domains if you create a music or email app. When you type the [`AppIntent(schema:)`](appintent(schema:).md) macro in your source file and specify a schema from one of the domains, Xcode code completion generates the initial code for your app intent, including any expected parameters. These templates simplify the creation of your code and help your app work seamlessly with Apple Intelligence and Siri.

![A flow diagram that shows input flowing into an app intent’s perform method and the method’s output.](https://docs-assets.developer.apple.com/published/23a505e82503bfc6f1a0148037260f98/getting-started-with-the-app-intents-framework-2%402x.png)

Whether you define a custom app intent or use one of the predefined schemas, the [`AppIntent`](appintent.md) protocol defines the common behaviors for all app intents. Use this protocol, or one of several [`App intent types`](app-intent-types.md) as the starting point for your app intent type. Extend the features of your type by adding support for any of the other protocols the framework offers. Each app intent you create needs to have the following minimum set of behaviors:

- It performs an action in its [`perform()`](appintent/perform().md) method.
- It returns a result or error to tell the system whether the action succeeded or failed.
- It declares any required or optional parameters it needs to perform the action.
- It provides a localized title and other descriptive information that Siri, the Shortcuts app, and other system features can display.

For more information about defining and implementing app intents for your app, see [`Creating your first app intent`](creating-your-first-app-intent.md). For additional information about how to implement app intents, see [`App intents`](app-intents.md).

##### Express Your Apps Custom Data Types Using App Entities

Every app uses data objects to manage key information and the app creates and manages those objects at runtime. A fitness app might create a data object for each workout session, and track the workout duration and effort in that object. An email or messaging app might use data objects to track the contents of a message or its recipients. A web browser might use data objects to manage visible tabs or someone’s personal bookmarks. An *app entity* is a lightweight version of one of your data objects, and the system uses the app entities you create as a gateway to your app’s data.

![An illustration that shows how app entities move between your app, Siri, and other apps.](https://docs-assets.developer.apple.com/published/764f24f34832fec77407534eafd51ebb/getting-started-with-the-app-intents-framework-3%402x.png)

App entities provide access to your app’s data, but your actual data objects remain the source of truth. You typically create entities for only a subset of your app’s actual data, focusing on the types that people see and manipulate from your interface. The app entity type you create using the [`AppEntity`](appentity.md) protocol then reflects your app’s data. If your app’s data objects are lightweight, you might update them to support this protocol directly. However, the more common approach is to define custom entity types that refer to your app’s existing types, and use them to provide access to your data.

Define custom app entities for any data types that are unique to your app, but build app entities for common data types using the schemas in the [`App schema domains`](app-schema-domains.md) and the types in the App Intents framework. The domain-based schemas define the properties the system expects for your app entities. When you type the [`AppEntity(schema:)`](appentity(schema:).md) macro in your source file and specify a schema from one of the domains, Xcode code completion generates the initial code for your app entity. Each app entity type has the following minimum set of responsibilities:

- It stores a unique identifier that your app can use to locate the underlying data.
- It offers a query object to find specific instances of itself.
- It defines properties for key variables.
- It provides descriptive information the system can display to people.

Query objects help the system find your app entities at runtime. For each of your app entities, you provide query objects to search for one with a specific identifier or matching a specific value. System features like Siri use your queries to try and resolve conversational requests automatically. For example, if a request involves a document with a specific name, Siri uses your query to search for a document entity with that name.

> ❗ **Important**: Make your app entity types transferable to support exchanging them with other processes. For more information about adding transferable support, see the [`Core Transferable`](https://developer.apple.com/documentation/CoreTransferable) framework.

##### Wrap Finite Lists of Options in App Enums

Many apps use enumerations or static types to define constants with special meaning. An *app enum* is a lightweight version of that type you use to define app intent parameters or app entity properties. A shopping app might use an app entity to represent an item of clothing someone can purchase, and use an app enum to represent the possible sizes for those clothes. Similarly, an app entity for a calendar invitation might include a variable with an app enum to indicate whether the person accepted, declined, or is tentative about the meeting.

An app enum’s main job is to provide descriptive information about its options, which the system uses to present those options in system interfaces. For example, it might display those descriptions as possible options for resolving an app intent parameter. When defining an app enum, make sure your type adheres to the following rules:

- The type inherits from the [`AppEnum`](appenum.md) type.
- Its storage type is [`String`](https://developer.apple.com/documentation/Swift/String).
- The type also conforms to the [`RawRepresentable`](https://developer.apple.com/documentation/Swift/RawRepresentable) protocol.

For more information about how to create app enums, see [`App enums`](app-enums.md).

##### Improve the App Intent Experience with App Shortcuts

App Shortcuts provide a polished experience for people wanting to use your app’s actions from the Shortcuts app and other places in the system. An App Shortcut is a combination of an app intent with some additional data, such as spoken phrases that trigger an app intent in Siri. People run them on their own or combine them in the Shortcuts app to create custom workflows.

To provide App Shortcuts for your app intents, create a type that conforms to the [`AppShortcutsProvider`](appshortcutsprovider.md) protocol. In your type, create an [`AppShortcut`](appshortcut.md) type for each of your app intents. The compiler extracts your code and makes it available to the Shortcuts app and the rest of the system. App Shortcuts typically have a localized title and description to help people understand what it does. You can also add values to customize the appearance of your App Shortcuts and specify other details.

For more information about creating App Shortcuts, see [`App Shortcuts`](app-shortcuts.md).

##### Run App Intents in the Foreground and Background

Some app intents require your app to run in the foreground, but many can run quietly in the background. Rather than require your app to run every time, you can provide an [`App extension`](app-extension.md) to run some of your app intents in the background. Providing an app extension helps minimize disruptions, especially in iOS, iPadOS, tvOS, visionOS, and watchOS when another app is already in the foreground.

If an app intent can run in both the foreground and background, consider placing its code in a Swift package or library that you share between your app and app extension. Configure the [`supportedModes`](appintent/supportedmodes.md) property of each app intent with preferences for when to run in the foreground and when to run in the background. Modes give you a configurable way to run app intents in the background, but transition to the foreground to present UI or perform tasks that require someone’s attention.

> **Note**: Some intents require your app to run in the foreground, and automatically launch your app if it’s not running. For example, the [`OpenIntent`](openintent.md) protocol defines an app intent that launches your app to display a specific item. Place the code for these app intents only in your app.

##### Donate App Intents and App Entities to the System

Some system features use a person’s past actions to suggest actions they might want to take in the future. When someone uses the Shortcuts app or a feature like Siri to run app intent code, the system collects the app intents and uses them to generate suggestions. In your app, make similar donations when someone performs actions through your app’s interface. Your donations give the system a more complete picture of the actions that someone cares about, and help the system improve its suggestions.

An app can also donate app entities to give the system additional context about your app’s content. When indexing your app’s content using Core Spotlight, include app entities so the system knows where to find your app’s data. When configuring the views of your interface, include app entities to reflect the content someone is seeing in those views. For example, if your music app’s interface is currently displaying a song in a view, attach the app entity for that song to the view. If someone asks Siri to “play this song”, Siri can use that contextual information to play the song without asking for more information.

For more information about donating app intents and app entities, see [`Donations and discovery`](donations-and-discovery.md).

##### Offer Visual Representations of Your Content

System features like Siri and the Shortcuts app display information from your app intents and entities visually. If someone uses Siri while looking at their iPhone, the system might choose to display results visually in addition to speaking those results. If you want to provide a more visually engaging interface for your custom content, provide a *snippet* for your app intent, which is a set of SwiftUI views you create programmatically and include with your app intent.

An app intent can also use snippets to request confirmation for a particular value or to display the final results of the action. If you return a snippet from the [`perform()`](appintent/perform().md) method of your intent, features like Siri can use that snippet to display the results.

For information about creating snippets and other visual elements for your app intents and entities, see [`Visual presentation`](visual-presentation.md).

##### Provide a Deeper Integration with System Features

The app intents, app entities, and app enums you create provide the foundational code you need to interact with the other parts of the system. To make sure your code integrates well with specific features, review the requirements for that feature and make sure you add the relevant support to your code. For example:

- [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md) work better for app intents that support a known [`App schema domains`](app-schema-domains.md).
- [`Spotlight integration`](spotlight.md) uses entity donations to support enhanced interactions with your app.
- The [`App Shortcuts`](app-shortcuts.md) experience is better when you provide specific details.
- [`Widgets, Live Activities, and Controls`](widgets-live-activities-and-controls.md) can use app intents to support interactive controls.
- Customize the [`Hardware interactions`](hardware-interactions.md) behaviors on iPhone using app intents.
- Respond to [`Focus`](focus.md) mode changes using app intents.
- Classify your app’s content, and make that information available to [`Visual intelligence`](visual-intelligence.md) using app intents.

## See Also

- [App Intents updates](../Updates/AppIntents.md)
  Learn about important changes in App Intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework)*