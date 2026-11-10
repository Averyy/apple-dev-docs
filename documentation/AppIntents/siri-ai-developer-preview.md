# Siri AI Developer Preview

**Framework**: App Intents  
**Role**: API Collection

Bring custom actions and content to Siri AI.

## Overview

With the Siri AI Developer Preview, Siri can understand context, find content, and perform actions not only for functionality and data that fits system-defined app schema domains, but also for custom actions and information. The Developer Preview supports the following:

**Requests that don’t include your app.** People don’t have to mention your app in their request while your app is in the foreground, while a Live Activity is active, or when a person continues a conversation in the Siri app that includes a mention of your app.

For example, a person might request a ride with a ride share app, follow updates to the app’s Live Activity while they wait for their ride to arrive, then request to move the pickup location to a different address by saying

**While your app is in the background, requests need to mention your app.** Siri can find custom content and perform actions when your app is in the background if someone mentions your app in their request. For example, a person might say:

Siri understands that the person liked a pair of sneakers in the mentioned app and provides the information.

**Requests can include actions across apps.** Siri can find custom content from one app, transfer it to another app, and perform an action. For example, somebody might request:

Siri finds sneakers that the person added to their favorites, understands who the partner is, finds them in Contacts, then sends the sneaker information to them using the messaging app.

## Developer Preview availability

The Siri AI Developer Preview is available in iOS, iPadOS, macOS, and visionOS, on devices that support Apple Intelligence, and in regions where Apple Intelligence and Siri AI are available.

> ❗ **Important**: During the Siri AI Developer Preview, the App Intents API and Siri functionality may change.

Test your integration with the new Siri AI capabilities using the following methods:

- Build your app with Xcode, sign it with a development profile, and run it on a device that supports the Siri AI Developer Preview.
- Make versions of your app available to internal testers in TestFlight.

The Siri AI Developer Preview isn’t available to external testers in TestFlight or to versions of your app that you publish on the App Store. If you distribute a version of your app that uses App Intents API to integrate custom actions and content with Siri, Siri AI Developer Preview functionality isn’t available to external testers or people who get your app from the App Store. For more information about distributing apps to internal testers, see [App Store Connect Help](https://developer.apple.com/help/app-store-connect/test-a-beta-version/add-internal-testers).

## Custom actions, content, and snippets in Siri

Siri can only find custom content and perform custom actions an app makes explicitly available using App Intents. To make your custom app intents and entities available to the Siri AI Developer Preview, update your existing App Intents code as described in [Bringing custom actions and content to Siri](./bringing-custom-actions-and-content-to-siri.md).

Siri displays custom content a person requests in card snippets that you provide. The card snippets include the requested information and use your custom views to show your app’s branding and personality. For more information, see [`CardSnippet`](./cardsnippet.md).

## Extra guidance for complex actions

To perform complex custom actions and handle unique content that people include in ambiguous requests, Siri might need additional guidance to understand your app’s unique domain. For example, to perform the same action with Siri, someone might use either of the following to form their request:

To provide additional guidance to Siri for complex tasks, create app skills as described in [Orchestrating complex actions with app skills](./orchestrating-complex-actions-with-app-skills.md).

## Siri Integration Advisor and Siri Evaluations

The Siri AI Developer Preview includes features to help you improve how your app intents work with Siri:

- The Siri Integration Advisor in Xcode provides feedback and suggestions that help you improve your App Intents implementation to enable Siri to perform your app’s custom actions and handle its custom data.
- The [Siri Evaluations](../sirievaluations/sirievaluations.md) framework lets you script requests to Siri, measure how Siri handles them, and catch changes in how Siri responds as you update your intents and entities.

## Topics

### Getting started
- [Bringing custom actions and content to Siri](./bringing-custom-actions-and-content-to-siri.md)
  Support the Siri AI Developer Preview by turning custom app intents into tools Siri can call, and by helping Siri understand your app entities.
- [Orchestrating complex actions with app skills](./orchestrating-complex-actions-with-app-skills.md)
  Guide Siri AI through a complex task that involves several tool intents by providing an app skill.
### Tool support
- [macro AppIntent(AppIntentTraits)](./appintent%28_%29.md)
  Makes an existing app intent available to Siri as a tool.
- [macro AppIntent<T>(AppIntentTraits, schema: T)](./appintent%28_,schema%29.md)
  Makes an app intent that conforms to a schema available to Siri as a tool.
- [struct AppIntentTraits](./appintenttraits.md)
  The roles an app intent takes on, passed to `@AppIntent`.
- [struct IntentVisibility](./intentvisibility.md)
  A value that configures how a property is available to system features, such as Siri and Shortcuts, if at all.
- [protocol ToolIntent](./toolintent.md)
  A protocol that identifies an app intent that Siri can call while handling a person’s request.
### Entity support
- [protocol GenerableEntity](./generableentity.md)
  An interface that tells a model it can create an entity and fill in its properties directly.
- [macro AppEntity(AppEntityTraits)](./appentity%28_%29.md)
  Marks a transient entity whose values the model can generate on its own.
- [macro AppEntity<T>(AppEntityTraits, schema: T)](./appentity%28_,schema%29.md)
  Marks a transient entity that conforms to a schema as one whose values the model can generate on its own.
- [macro ComputedProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?)](./computedproperty%28title,description,authenticationpolicy,visibility%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?, customIndexingKey: CSCustomAttributeKey)](./computedproperty%28title,description,authenticationpolicy,visibility,customindexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./computedproperty%28title,description,authenticationpolicy,visibility,indexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro DeferredProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?)](./deferredproperty%28title,description,authenticationpolicy,visibility%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./deferredproperty%28title,description,authenticationpolicy,visibility,indexingkey%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [struct AppEntityTraits](./appentitytraits.md)
  The roles an app entity takes on, passed to `@AppEntity`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siri-ai-developer-preview)*