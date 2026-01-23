---
url: https://developer.apple.com/design/human-interface-guidelines/app-shortcuts
framework: HIG
---

# App Shortcuts

**Type:** article

**Platforms:** ios, ipados, visionos, watchos

> **Updated 2025-01-17:** Updated and streamlined guidance.

An App Shortcut gives people access to your app’s key functions or content throughout the system.

![A stylized representation of the Notes app appearing as the result in the Top Hit area of Spotlight, along with App Shortcuts for creating a new note and opening two other recent notes. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/5dc7a4f5729b780f2288a9ae93c28f1c/components-app-shortcuts-intro~dark%402x.png)
People can initiate App Shortcuts using features like [Siri](siri.md), Spotlight, and the Shortcuts app; using hardware features like the [Action button](action-button.md) on iPhone or Apple Watch; or by [Squeeze](apple-pencil-and-scribble.md#Squeeze) Apple Pencil.
Because App Shortcuts are part of your app, they are available immediately when installation finishes. For example, a journaling app could offer an App Shortcut for making a new journal entry that’s available before a person opens the app for the first time. Once someone starts using your app, its App Shortcuts can reflect their choices, like those from FaceTime for calling recent contacts.
![A partial screenshot of the Shortcuts app on iPhone showing App Shortcuts for FaceTime listed in a grid view. The App Shortcuts are in a group labeled Call Recents, and are each titled with the name of a recent FaceTime contact.](https://docs-assets.developer.apple.com/published/e1dd13b73fe99997226c00130ca6d2d3/app-shortcuts-personalized-choices~dark%402x.png)
App Shortcuts use [App Intents](../AppIntents.md) to define actions within your app to make available to the system. Each App Shortcut includes one or more actions that represent a set of steps people might want to perform to accomplish a task. For example, a home security app might combine the two common actions of turning off the lights and locking exterior doors when a person goes to sleep at night into a single App Shortcut. Each app can include up to 10 App Shortcuts.

> **Note:** When you use App Intents to make your app’s actions available to the system, in addition to the App Shortcuts that your app provides, people can also make their own custom shortcuts by combining actions in the Shortcuts app. Custom shortcuts give people flexibility to configure the behavior of actions, and enable workflows that perform tasks across multiple apps. For additional guidance, see the [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios).

## Best practices
**Offer App Shortcuts for your app’s most common and important tasks.** Straightforward tasks that people can complete without leaving their current context work best, but you can also open your app if it helps people complete multistep tasks more easily.
**Add flexibility by letting people choose from a set of options.** An App Shortcut can include a single optional value, or parameter, if it makes sense. For example, a meditation app could offer an App Shortcut that lets someone begin a specific type of meditation: “Start [morning, daily, sleep] meditation.” Include predictable and familiar values as options, because people won’t have the list in front of them for reference. For developer guidance, see [Adding parameters to an app intent](../AppIntents/Adding-parameters-to-an-app-intent.md).
![A diagram of the activation phrase of a shortcut for ordering a drink from a coffee app. The activation phrase contains an optional value for the name of the drink, which is underlined and called out as the shortcut's parameter.](https://docs-assets.developer.apple.com/published/c498310c2f20dc4e1dd2b5a2a9e7895c/app-intents-parameter-diagram~dark%402x.png)
**Ask for clarification in response to a request that’s missing optional information.** For example, someone might say “Start meditation” without specifying the type (morning, daily, or sleep); you could follow up by suggesting the one they used most recently, or one based on the current time of day. If one option is most likely, consider presenting it as the default, and provide a short list of alternatives to choose from if a person doesn’t want the default choice.
**Keep voice interactions simple.** If your phrase feels too complicated when you say it aloud, it’s probably too difficult to remember or say correctly. For example, “Start [sleep] meditation with nature sounds” appears to have two possible parameters: the meditation type, and the accompanying sound. If additional information is absolutely required, ask for it in a subsequent step. For additional guidance on writing dialogue text for voice interactions, see [Siri](siri.md).
**Make App Shortcuts discoverable in your app.** People are most likely to remember and use App Shortcuts for tasks they do often, once they know the shortcut is available. Consider showing occasional tips in your app when people perform common actions to let them know an App Shortcut exists. For developer guidance, see [SiriTipUIView](../AppIntents/SiriTipUIView.md).

### Responding to App Shortcuts
As a person engages with an App Shortcut, your app can respond in a variety of ways, including with dialogue that Siri speaks aloud and custom visuals like snippets and Live Activities.
- Snippets are great for custom views that display static information or dialog options, like showing the weather at a person’s location or confirming an order. For developer guidance, see [ShowsSnippetView](../AppIntents/ShowsSnippetView.md).
- [Live Activities](live-activities.md) offer continuous access to information that’s likely to remain relevant and change over a period of time, and are great for timers and countdowns that appear until an event is complete. For developer guidance, see [LiveActivityIntent](../AppIntents/LiveActivityIntent.md).
![A screenshot of the iPhone Home Screen with a custom snippet occupying the top half of the screen. The snippet includes buttons to confirm or cancel a delivery order from a coffee shop, along with the items in the order and the total price.](https://docs-assets.developer.apple.com/published/75e93052edfb5d72d2178146db119266/app-shortcuts-siri-dialogue~dark%402x.png)
![A screenshot of the iPhone Home Screen with a Live Activity occupying the top quarter of the screen. The Live Activity shows the estimated time for the arrival of a delivery of an order from a coffee shop, along with the number of items in the order and a button to contact the delivery driver.](https://docs-assets.developer.apple.com/published/b05baec2e9b73902f37ca7797f10b4eb/app-shortcuts-live-activity~dark%402x.png)
**Provide enough detail for interaction on audio-only devices.** People can receive responses on audio-only devices such as AirPods and HomePod too, and may not always be able to see content onscreen. Include all critical information in the full dialogue text of your App Shortcuts. For developer guidance, see [init(full:supporting:systemImageName:)](../AppIntents/IntentDialog/init(full:supporting:systemImageName:).md).

## Editorial guidelines
**Provide brief, memorable activation phrases and natural variants.** Because an App Shortcut phrase (or a variant you define) is what people say to run an App Shortcut with Siri, it’s important to keep it brief to make it easier to remember. You have to include your app name, but you can be creative with it. For example, Keynote accepts both “Create a Keynote” and “Add a new presentation in Keynote” as App Shortcut phrases for creating a new document. For developer guidance, see [AppShortcutPhrase](../AppIntents/AppShortcutPhrase.md).
**When referring to App Shortcuts or the Shortcuts app, always use title case and make sure that *Shortcuts* is plural.** For example, *MyApp integrates with Shortcuts to provide a quick way to get things done with just a tap or by asking Siri, and offers App Shortcuts you can place on the Action button.*
**When referring to individual shortcuts (not App Shortcuts or the Shortcuts app), use lowercase.** For example, *Run a shortcut by asking Siri or tapping a suggestion on the Lock Screen.*

## Platform considerations
*No additional considerations for visionOS or watchOS. Not supported in tvOS.*

### iOS, iPadOS
App Shortcuts can appear in the Top Hit area of Spotlight when people search for your app, or in the Shortcuts area below. Each App Shortcut includes a symbol from [SF Symbols](sf-symbols.md) that you choose to represent its functionality, or a preview image of an item that the shortcut links to directly.
![A partial screenshot showing search results in Spotlight on iPhone, including the Top Hit area at the top of the screen with the Suggestions area beneath it. The Notes app appears as the Top Hit, with App Shortcuts appearing in a row to the right of the app icon: one titled New Note with a symbol of a pencil diagonally over a square, one titled Quick Note with a symbol of a scribbled line on a canvas, and one with a thumbnail of an embedded image for a recent note titled Nature. The Suggestions area includes a link to a web search for 'not,' and suggested autocomplete terms 'noteworthy' and 'notes'.](https://docs-assets.developer.apple.com/published/11e4814bf124943b889fc4f56a025431/app-shortcuts-spotlight-search-top-hit%402x.png)
**Order shortcuts based on importance.** The order you choose determines how App Shortcuts initially appear in both Spotlight and the Shortcuts app, so it’s helpful to include the most generally useful ones first. Once people start using your App Shortcuts, the system updates to prioritize the ones they use most frequently.
**Offer an App Shortcut that starts a Live Activity.** Live Activities allow people to track an event or the progress of a task in glanceable locations across their devices. For example, a cooking app could offer a Live Activity to show the time left until a dish is ready to take out of the oven. To make it easy for people to start a cooking timer, the app offers an App Shortcut that people can place on the Action button. For more information about Live Activities, see [Live Activities](live-activities.md).

### macOS
App Shortcuts aren’t supported in macOS. However, actions you create for your app using App Intents are supported, and people can build custom shortcuts using them with the Shortcuts app on Mac.

## Resources

#### Related
[Siri](siri.md)
[Siri Style Guide](https://developer.apple.com/siri/style-guide/)
[Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)

#### Developer documentation
[App Intents](../AppIntents.md)
[SiriKit](../SiriKit.md)
[Making actions and content discoverable and widely available](../AppIntents/Making-actions-and-content-discoverable-and-widely-available.md) — App Intents
[Integrating custom data types into your intents](../AppIntents/Integrating-custom-types-into-your-intents.md) — App Intents

#### Videos
- [Design interactive snippets](https://developer.apple.com/videos/play/wwdc2025/281) - Snippets are compact views invoked from App Intents that display information from your app. Now, snippets can allow your app to bring even more capability to Siri, Spotlight, and the Shortcuts app by including buttons and stateful information that offer additional interactivity as part of an intent. In this session, you’ll learn best practices for designing snippets, including guidance on layout, typography, interaction, and intent types.
- [Get to know App Intents](https://developer.apple.com/videos/play/wwdc2025/244) - Learn about the App Intents framework and its increasingly critical role within Apple’s developer platforms. We’ll take you through a ground-up introduction of the core concepts: intents, entities, queries, and much more. You’ll learn how these pieces fit together and let you integrate your app through Apple’s devices, from software features like Spotlight and Shortcuts to hardware features like the Action button. We’ll also walk through how App Intents is your app’s gateway to integrating with Apple Intelligence going forward.
- [Bring your app’s core features to users with App Intents](https://developer.apple.com/videos/play/wwdc2024/10210) - Learn the principles of the App Intents framework, like intents, entities, and queries, and how you can harness them to expose your app’s most important functionality right where people need it most. Find out how to build deep integration between your app and the many system features built on top of App Intents, including Siri, controls and widgets, Apple Pencil, Shortcuts, the Action button, and more. Get tips on how to build your App Intents integrations efficiently to create the best experiences in every surface while still sharing code and core functionality.

## Change log
| Date | Changes |
| --- | --- |
| January 17, 2025 | Updated and streamlined guidance. |
| June 5, 2023 | New page. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/app-shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts)*
