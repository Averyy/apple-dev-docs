# Donations and discovery

**Framework**: App Intents

Donate your app’s intents and entities to the system to help it identify trends and predict future behaviors.

#### Overview

When someone performs an action in your app’s interface, create a matching app intent and donate it to the system. Donations help the system analyze a person’s current actions and predict their future actions. For example, if someone asks your app for the weather each morning, the system might proactively suggest the same action each morning. Restrict your donations to direct interactions with your app’s interface, and not to interactions started by Siri or the Shortcuts app.

You can also improve the quality of your app’s searchable content by donating app entities to the system. Donate entities to Spotlight with the rest of your app’s content so the system can use them to display content directly in your app. In your app’s interface, associate entities with views to communicate the data your app currently shows. Apple Intelligence and Siri use your donations to improve conversational results.

## Topics

### Essentials
- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)
  Improve how people interact with your app through Apple Intelligence and Siri by teaching the system about your app’s data and actions.
### Donation management
- [struct IntentDonationManager](intentdonationmanager.md)
  A type you use to teach the system about the actions people take using your app.
- [struct IntentDonationIdentifier](intentdonationidentifier.md)
  An opaque type that identifies a specific donation to the system.
- [struct IntentDonationMatchingPredicate](intentdonationmatchingpredicate.md)
  A type you use to specify previously donated app intents.
### Spotlight donations
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Update your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.
### Onscreen context
- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)
  Annotate your interface with app entities to offer contextual information about your app’s onscreen content.
### Intent relevance
- [struct RelevantIntent](relevantintent.md)
  A type that stores an app intent and indicates its relevance to someone.
- [class RelevantIntentManager](relevantintentmanager.md)
  A type you use to suggest app intents and their current relevance to a person.
- [struct RelevantContext](../RelevanceKit/RelevantContext.md)
  Contextual clues the system uses to show relevant widgets in the Smart Stack on watchOS.
### Entity relevance
- [struct RelevantEntities](relevantentities.md)
  A type you use to donate your app’s songs, albums, artists, and other media items to play during workouts.
- [struct AppEntityContext](appentitycontext.md)
  The context used to scope suggested entity donations to a specific domain.
- [struct AudioContext](audiocontext.md)
  Specifies the type of audio activity to associate with a suggested entity, allowing the system to surface relevant suggestions at the right moment.

## See Also

- [App schema domains](app-schema-domains.md)
  Declare support for well-known actions and content by applying system-defined schemas to your app intents, app entities, and app enumerations.
- [Visual presentation](visual-presentation.md)
  Display app intents and app entities visually using snippets, and associate intents and entities with your app’s scenes and views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/donations-and-discovery)*