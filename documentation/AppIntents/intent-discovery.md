# Intent discovery

**Framework**: App Intents

Donate your app’s intents to the system to help it identify trends and predict future behaviors.

#### Overview

Make your intents more discoverable to people by donating them to the system. When someone performs an action in your app, donate an intent that corresponds to that action. The system uses the information you provide to predict actions someone might take in the future. For example, if someone requests the weather from your app each morning, the system might proactively offer the corresponding app intent at the same time each day.

Donate intents only when someone uses your app’s interface directly. You don’t need to donate intents associated with Siri or interactions with the Shortcuts app because the system donates them automatically. You can also delete donations when someone cancels or reverses a previously executed action, or when the action is no longer relevant.

## Topics

### Donation management
- [struct IntentDonationManager](intentdonationmanager.md)
  A type you use to donate intents to the system, or delete intents when they become irrelevant.
- [struct IntentDonationIdentifier](intentdonationidentifier.md)
  An opaque type that identifies a specific donation to the system.
- [struct IntentDonationMatchingPredicate](intentdonationmatchingpredicate.md)
  The match conditions that identify a set of previously donated app intents.
### Intent predictions
- [protocol PredictableIntent](predictableintent.md)
  An interface that allows the system to suggest the app intent to someone in the future using predictions you provide.
- [struct IntentPrediction](intentprediction.md)
  A prediction for a specific app intent that the system might display to someone when it’s relevant.
### Intent relevancy
- [struct RelevantIntent](relevantintent.md)
  A type that specifies an intent and its relevance to the user.
- [class RelevantIntentManager](relevantintentmanager.md)
  A type that saves relevant intents.
- [struct RelevantContext](../RelevanceKit/RelevantContext.md)
  Contextual clues the system uses to show relevant widgets in the Smart Stack on watchOS.

## See Also

- [Making your app’s functionality available to Siri](making-your-app-s-functionality-available-to-siri.md)
  Add app intent schemas to your app so Siri can complete requests, and integrate your app with Apple Intelligence, Spotlight, and other system experiences.
- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
  Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence.
- [Making onscreen content available to Siri and Apple Intelligence](making-onscreen-content-available-to-siri-and-apple-intelligence.md)
  Enable Siri and Apple Intelligence to respond to a person’s questions and action requests for your app’s onscreen content.
- [App intent domains](app-intent-domains.md)
  Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intent-discovery)*