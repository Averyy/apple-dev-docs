# Bringing custom actions and content to Siri

**Framework**: App Intents  
**Role**: Article

Support the Siri AI Developer Preview by turning custom app intents into tools Siri can call, and by helping Siri understand your app entities.

## Overview

With the Siri AI Developer Preview, Siri can use your app’s custom app intents and entities to respond to complex requests people make using natural language. Siri can only find content and perform actions you make available explicitly. To bring your app’s custom actions to Siri AI, identify the app intents you want to make available. Then, add the Swift macro to turn them into tools Siri can use.

> ❗ **Important**: The Siri AI Developer Preview is available in iOS, iPadOS, macOS, and visionOS on devices that support Apple Intelligence. During the preview, the App Intents API and Siri functionality may change.

When a person makes a request to Siri, it needs to match what a person says or types with your app’s actions and content. Update app intents and entities with additional information like titles and descriptions that people might use in their requests or that Siri should include in responses.

To perform your app’s custom actions and let people find your app’s custom content, Siri needs to find your app’s custom content to respond to a person’s request. To let Siri find your custom content, make your app entities available to Spotlight.

Additionally, provide Siri with onscreen context and behavioral cues so people can refer to your app’s visible content in their requests or use ambiguous phrases, and let Siri pass custom app entities from one app intent to another by providing transferable representations.

## Turn custom intents into tools Siri can use

Siri can only perform actions you make explicitly available. To bring your app’s custom actions to Siri, add the `@AppIntent(.tool)` Swift macro to a new or existing app intent. The macro adds conformance to the [`ToolIntent`](./toolintent.md) protocol, which makes the intent available as a tool to Siri.

Which intents you make available to Siri is up to you. Consider making your app’s key functionality and any other functionality a person might want to perform with Siri available.

If you already make an app intent available to Siri by conforming it to a schema in a primary domain listed in [App schema domains](./app-schema-domains.md), don’t add the `@AppIntent(.tool)` Swift macro. By adopting a schema that supports Siri, you already make the action available to Siri. For example, if your messaging app implements the [`sendMessage`](./appschema/messagesintent/sendmessage.md) schema, don’t add tool intent conformance to the intent.

If an app intent serves a specific purpose and doesn’t perform a custom action in its `perform()` implementation, don’t add the tool intent annotation either. For example, the purpose of a [`WidgetConfigurationIntent`](./widgetconfigurationintent.md) is to make a widget configurable. It usually doesn’t include a `perform()` implementation and can’t be a tool intent because there’s no action for Siri to perform. If you use your `WidgetConfigurationIntent` for a custom action and it contains a `perform()` implementation, you can turn it into a tool intent.

## Provide additional information for app intents

In addition to telling Siri that your app contains an action it can perform, Siri needs to know what the intent does, how to fill in its parameters, and how to disambiguate it from other intents. To understand what your intent does and disambiguate from other intents, Siri relies on its [`title`](./appintent/title.md) and [`description`](./appintent/description.md). If you don’t already provide a `title` and a `description` for your custom intent, add them. To tell Siri how it can perform your app intent, what information it needs, and how to present intent parameters, provide a `title` and `description` for each parameter.

This example shows how a tool intent for a shopping app might provide titles and descriptions for a tool intent and its parameters. It enables people to use Siri to add an item to a shopping cart:

```swift
@AppIntent(.tool)
struct AddToCart: AppIntent {
    static let title: LocalizedStringResource = "Add to Cart"
    static let description = IntentDescription(
        LocalizedStringResource("Adds a product to the shopping cart.")
    )

    @Parameter(title: "Item", description: LocalizedStringResource("The product to add"))
    var item: ProductEntity

    @Parameter(title: "Quantity", description: LocalizedStringResource("How many to add"), default: 1)
    var quantity: Int

    func perform() async throws -> some IntentResult {
        try await Cart.shared.add(item, quantity: quantity)
        return .result()
    }
}
```

Some [App schema domains](./app-schema-domains.md) provide schemas that support Shortcuts but not Siri. If your intent conforms to such a schema, turn it into a tool intent that Siri can perform by annotating it with `@AppIntent(.tool, schema:)`. For example, if your journaling app implements the [`createEntry`](./appschema/journalintent/createentry.md) schema, replace the `@AppIntent(.journal.createEntry)` annotation with `@AppIntent(.tool, schema: .journal.createEntry)` as shown in this example:

```swift
@AppIntent(.tool, schema: .journal.createEntry)
struct CreateEntryIntent {
    // ...
}
```

For more information about app schema domains, see [App schema domains](./app-schema-domains.md).

## Add information to your app entities

Siri relies on the `title` and `description` you provide for a tool intent and its parameters to disambiguate it from other intents, present it to a person, and perform its action. The same concept applies to custom app entities.

To understand custom content, match it to a person’s request, provide it as a response, and disambiguate between app intents, Siri relies on additional information you provide for your custom app entities. In addition to a `title`, pass a `description` to each `@Property`, `@DeferredProperty`, and `@ComputedProperty` of your app entities.

By default, app entities don’t require authentication before Shortcuts or Siri present entity information. However, information an app entity describes, like any financial information, can be sensitive. For entity properties a person might want to keep private, require Siri to request authentication before it presents a response that includes the entity or shows some of its properties. To require authentication, declare a custom [`IntentAuthenticationPolicy`](./intentauthenticationpolicy.md):

- To define an `IntentAuthenticationPolicy` that applies to the whole entity and its properties, override the default authentication policy by declaring a static `authenticationPolicy` property and setting its value to the policy you want; for example, [`IntentAuthenticationPolicy.requiresAuthentication`](./intentauthenticationpolicy/requiresauthentication.md).
- To define an `IntentAuthenticationPolicy` that applies to a specific property, pass the appropriate `IntentAuthenticationPolicy` to the `@Property`, `@DeferredProperty`, or `ComputedProperty` Swift macro.

> **Note**: The authentication policy you set for a specific property only applies to responses Siri provides. If your app intent returns sensitive information as its intent result, set the policy on the intent-level to require authentication.

Sometimes, an entity might contain a property that you don’t want to make available to Siri and other system experiences at all; for example, an entity property might not have a use outside of your app. To make a property available only to your app and its extensions, such as its widgets and controls, provide the property Swift macro with a `visibility` value of [`internal`](./intentvisibility/internal.md). Siri, Shortcuts, and other system features don’t surface or read internal entity properties.

This example shows how a finance app might make an app entity that describes a bank account available to Siri. The entity explicitly defines its `authenticationPolicy` on the entity level as `.alwaysAllowed` and requires authentication before showing sensitive information. The `routingNumber` property is only accessible to the app and its extensions.

```swift
struct BankAccount: AppEntity {
    static let authenticationPolicy: IntentAuthenticationPolicy =
        .alwaysAllowed

    @Property(
        title: "Nickname",
        description: "The name the account holder gave this account.",
        authenticationPolicy: .requiresAuthentication
    )
    var nickname: String

    @Property(
        title: "Balance",
        description: "The current balance, including pending transactions.",
        authenticationPolicy: .requiresLocalDeviceAuthentication
    )
    var balance: IntentCurrencyAmount

    @Property(title: "Branch", authenticationPolicy: .requiresAuthentication)
    var branch: String

    @Property(title: "Routing Number", visibility: .internal)
    var routingNumber: String
}
```

## Let Siri fill an app entity from a request

When you create a tool intent and provide descriptions for intent and entity properties, Siri understands your custom content and includes it in responses. Siri can also fill an app entity with information people include in their request. This lets Siri create the entity directly, rather than by asking your app’s query objects to return it. For example, consider the phrase:

Siri creates a generable app entity that the airline app defines. Siri then passes the app entity to the app intent for finding the flight. The airline app doesn’t have to create the app entity itself. To enable Siri so it fills in your tool intent’s parameters without first querying your app, conform your app entity to [`GenerableEntity`](./generableentity.md) and [`TransientAppEntity`](./transientappentity.md) by adding a [`generable`](./appentitytraits/generable.md) app entity trait using the `@AppEntity(.generable)` macro, as shown here:

```swift
@AppEntity(.generable)
struct FlightSearch: TransientAppEntity {
    static let typeDisplayRepresentation: TypeDisplayRepresentation =
        "Flight Search"

    @Property(title: "Origin", description: "IATA code of the departure airport")
    var origin: String

    @Property(title: "Destination", description: "IATA code of the arrival airport")
    var destination: String

    @Property(title: "Date", description: "The day to depart")
    var date: Date

    @Property(title: "Cabin", description: "The cabin class to search")
    var cabin: CabinClass  // An app enumeration with the different class types.

    var displayRepresentation: DisplayRepresentation {
        "\(origin) → \(destination)"
    }

    init() {}
}
```

> ❗ **Important**: Make sure your [`generable`](./appentitytraits/generable.md) entity’s properties are also generable types. For more information, see [`GenerableEntity`](./generableentity.md).

## Enable Siri to find your app entities

To match a person’s request to your content, Siri needs to find the app entities that describe it. To enable Siri to find your app entities, make them available to Spotlight.

If you don’t include your entities in the Spotlight index, the system can also retrieve them from an [`EnumerableEntityQuery`](./enumerableentityquery.md) object you provide. The system can also find app intents for a parameter you configure with a [`DynamicOptionsProvider`](./dynamicoptionsprovider.md) type.

For more information about how to add entities to Spotlight, see [Making app entities available in Spotlight](./making-app-entities-available-in-spotlight.md).

## Provide onscreen context

People use Siri to interact with onscreen content, but that content is private to your app. Associating views, user activities, or other visible content with app entities gives Apple Intelligence *onscreen context*. For example, onscreen context lets someone refer to an onscreen photo conversationally as “this photo.”

With the Siri AI Developer Preview, you can provide onscreen context for custom app entities, not only for app entities that conform to an app schema, but the APIs you use to associate an app entity with views, user activities, and so on, are the same. For more information about providing onscreen context, see [Providing contextual cues to Apple Intelligence and Siri](./providing-contextual-cues-to-apple-intelligence-and-siri.md).

## Make actions discoverable

When people use Siri to perform a task, Apple Intelligence determines which of your app’s intents matches a request. In addition to information you provide for your tool intents and app entities, Siri uses behavioral cues you provide to Apple Intelligence to disambiguate app intents. When people perform actions in your app, donate their matching app intents to the system. For more information about providing behavioral cues, see [Donating your app’s data and actions to the system](./donating-your-apps-data-and-actions-to-the-system.md).

## Offer a transferable representation of your app entities

People use Siri to perform tasks across apps. Data that passes from one app to another needs to provide a representation that other apps can handle. For example, a person might say:

To respond to this request, Apple Intelligence handles flight information from an airline app, resolves contact information from the Contacts app, and makes the information available to the Mail app. As a result, the app entities that describe flight information and contact information conform to the [`Transferable`](../CoreTransferable/transferable.md) protocol and provide transferable representations.

Many Swift and system types already provide transferable representations. However, if your app intent uses custom app entities for its parameters or results, provide transferable representations for those entities. For more information about adopting the `Transferable` protocol, see [Core Transferable](../CoreTransferable/CoreTransferable.md).

## Verify your app’s integration with Siri AI

When you create app intents and entities, verify them with tests you write using the [App Intents Testing](../AppIntentsTesting/AppIntentsTesting.md) framework, and manually test them using the Shortcuts app, Spotlight, and Siri.

The Siri AI Developer Preview adds verification steps between tests you write with App Intents Testing and manual verification methods:

- The Siri Integration Advisor in Xcode provides feedback and suggestions that help you improve your App Intents implementation to enable Siri to perform your app’s custom actions and handle its custom data.
- The [Siri Evaluations](../sirievaluations/sirievaluations.md) framework lets you script requests to Siri, measure how Siri handles them, and catch changes in how Siri responds as you update your intents and entities.

For more information about verifying your App Intents code, see [Verifying your App Intents implementation](./verifying-your-app-intents-implementation.md).

## See Also

### Getting started
- [Orchestrating complex actions with app skills](./orchestrating-complex-actions-with-app-skills.md)
  Guide Siri AI through a complex task that involves several tool intents by providing an app skill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/bringing-custom-actions-and-content-to-siri)*