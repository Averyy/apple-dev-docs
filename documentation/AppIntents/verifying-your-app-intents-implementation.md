# Verifying your App Intents implementation

**Framework**: App Intents

Confirm that your app intents work correctly, the system can understand your content, and that it can run your app’s actions.

#### Overview

To verify the behavior of your App Intents code and integrations with system experiences, perform the following tasks to test different aspects of your App Intents implementation:

1. Write integration tests with the [`App Intents Testing`](https://developer.apple.com/documentation/appintentstesting) framework for code-level verification of your app intents and entities.
2. Check that app intents, their parameters, and their results appear correctly in the Shortcuts app.
3. Search for your entities in Spotlight to verify that Apple Intelligence and Siri can discover the entities that your app intents need and the ones that represent contextual cues you provide to Apple Intelligence and Siri.
4. Test the end-to-end Siri experience of [`App Shortcuts`](app-shortcuts.md) and app intents that conform to a schema in an [`App schema domains`](app-schema-domains.md).

The verification tasks above build on top of each other, and each step helps you catch different problems. For example:

- Integration tests confirm your `perform()` implementation returns an expected result, but they can’t tell you that a parameter summary reads awkwardly in the Shortcuts app.
- A custom shortcut with your intents in Shortcuts confirms your intent’s parameter representations and results, but it can’t verify the discoverability of your app entities.
- Spotlight confirms that your entities are discoverable, but it can’t verify that Siri correctly acts on a phrase people say.
- Verification of the end-to-end experience with Siri makes sure people can use natural language to perform your app’s actions.

> **Note**: On iPhone and iPad, Settings > Developer includes an option to display donations on the Lock Screen. This setting only applies to custom shortcuts you donate with [`SiriKit`](https://developer.apple.com/documentation/sirikit); it doesn’t apply to intents or entities you donate using App Intents.

#### Write Integration Tests with App Intents Testing

Create integration tests for your app intents code with the [`App Intents Testing`](https://developer.apple.com/documentation/appintentstesting) framework. App Intents Testing performs your code out-of-process, the same way Siri or Shortcuts perform them. As a result, it helps you verify the actual behavior of your app intents logic. To write tests for your app intents code:

1. Create tests that invoke the intents directly, including parameter values.
2. Assert on the result the same way you do with any other integration test.

Your App Intents code likely calls more general business logic like loading data from a database. To test your business logic, continue to use [`XCTest`](https://developer.apple.com/documentation/xctest) and [`Swift Testing`](https://developer.apple.com/documentation/testing).

For more information about using the App Intents Testing framework, see [`Testing your App Intents code`](https://developer.apple.com/documentation/appintentstesting/testing-your-app-intents-code).

#### Verify Intents Entities and Intent Results with the Shortcuts App

App intents by themselves don’t have a direct visual representation, and system experiences display intent parameters and their results differently based on a person’s device or context.

Shortcuts lets you verify that:

- Intents appear as actions under your app name in the Action Library, which is important because the system can only perform intents that it can find.
- Parameter summaries read like a natural sentence. The summary is a visual representation of your app intent that people read and edit, and you can’t verify awkward phrasing using code-level tests.
- Text you provide works well in each language you support; for example, use the direct visual presentation in Shortcuts to check if parameter summaries or the title of your intent work well.
- Intents handle inputs with correct and unexpected types for each parameter. For example, a parameter that accepts values it’s supposed to reject might be a bug that only shows up when a person edits the action.
- Parameter types flow through your intent correctly by chaining an intent with a follow-up action and confirming that the result flows through as the correct type.

> 💡 **Tip**: To verify that your intent works correctly as part of workflows across apps, create a cross-app shortcut that combines your intent with intents from other apps, and run it end-to-end.

To see a visual representation of your app intent in Shortcuts and use it to verify your app intents:

1. Build and run your app and wait for your app to launch.
2. Launch the Shortcuts app.
3. Tap or click the New Shortcut (+) button to create a custom shortcut.
4. Choose Apps in the Action Library’s segmented control.
5. Tap or click your app’s icon.
6. Select the action to test.
7. For app intents with parameters, use the summary that Shortcuts displays to set the parameter values.
8. Tap or click the Run button.

To debug issues when you run the intent in Shortcuts, set a breakpoint at the top of your `perform()` method before you run it. The debugger pauses execution immediately after you run the shortcut. Step through the code and, for example, inspect the intent’s parameters to verify they have the values they require.

#### Confirm That Entities and App Shortcuts Appear in Spotlight

To integrate your app with Apple Intelligence and Siri, donate your app entities to the Spotlight index and make them discoverable by the system. Then, manually test entity donations with Spotlight to verify that the system can find the data it needs to respond to a person’s request:

1. Use your app until it donates the entities you expect to find in a Spotlight search.
2. Open Spotlight on your device and search for text that matches an entity.
3. Tap a search result in Spotlight and confirm that it opens the corresponding scene in your app rather than just launching it.

Additionally, Spotlight allows you to verify your App Shortcuts. Make sure the phrases you define for an App Shortcut appear as Spotlight suggestions when you begin typing.

> **Note**: Spotlight indexing depends on device behavior that doesn’t always match Simulator. Validate Spotlight integration and entity discoverability on a physical device. To reset the Spotlight index and start Spotlight indexing from scratch, use the options that the device’s Developer settings provide in the CoreSpotlight Testing section.

For more information about making entities discoverable and integrating your app with Spotlight, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

#### Validate the End to End Experience with Siri

People can invoke actions using natural language with Apple Intelligence and Siri if you adopt app schemas for your intents, entities, and enums or provide App Shortcuts. To verify the integration with Apple Intelligence and Siri end-to-end, use Siri to test your app intents with phrases people actually say.

To use realistic phrases in your testing:

- Vary the wording and include filler words. Apple Intelligence typically maps these variations to the appropriate intent and resolves parameters to the correct entities.
- Try the same request with and without onscreen context. When an entity is visible onscreen and your app annotates its user activity or view, Siri can resolve references like “this” or “that” to the specific entity a person is looking at.
- Test requests that involve actions across multiple apps by asking Siri to run a request that invokes your app’s intent as one step of a larger workflow; the result from your intent then flows into the next action, just as it does in cross-app custom shortcuts.
- Test the most important workflows in a voice-only contexts such as with AirPods. In situations where there’s no screen to display the result of an intent, a verbal response has to convey the important details of that result. Refine the result of your intent until the audible reply is clear and provides the key information without being too lengthy.
- Test workflows with all languages that your app supports to make sure actions work well internationally.

## See Also

- [Testing your App Intents code](../appintentstesting/testing-your-app-intents-code.md)
  Evaluate intents, entities, and queries, and verify your integration with system features like Spotlight and Siri.
- [App Intents Testing](../appintentstesting/appintentstesting.md)
  Test your app intents, entities, queries, and integration with system features like Siri or Spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/verifying-your-app-intents-implementation)*