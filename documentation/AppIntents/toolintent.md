# ToolIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

A protocol that identifies an app intent that Siri can call while handling a person’s request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
protocol ToolIntent : AppIntent
```

## Mentions

- [Bringing custom actions and content to Siri](./bringing-custom-actions-and-content-to-siri.md)

## Overview

A *tool* is an [`AppIntent`](./appintent.md) that Siri can create, configure, and invoke to better respond to a person’s request. Siri can call a tool from a specific app when one or more situations apply to that app, such as:

- A person mentions the app by its name
- The app is in the foreground
- A relevant entity from that app appears in a search result

Think through which app intents are appropriate to promote to a tool. The best candidates are typically actions that a person can request in a single sentence, with parameters that Siri can fill in from that request. For example, an intent that adds a product to a shopping cart works well as a tool, because a person can say “Add two packs of AA batteries to my cart,” and Siri can fill in both the product and the quantity.

However, some intents don’t make good tools because they serve a different purpose or context. For example, the following app intents don’t apply to a person interacting with Siri:

- Widget configuration intents, which don’t invoke an action
- Intents that serve as a single step among others within a shortcut
- Intents with side effects that a person needs to start explicitly, such as placing an order and paying for it

Create a tool from one of your app’s existing intent types by passing the [`tool`](./appintenttraits/tool.md) trait to its `@AppIntent` macro:

```swift
@AppIntent(.tool)
struct AddToCart: AppIntent {
    static let title: LocalizedStringResource = "Add to Cart"
    static let description = IntentDescription("Adds a product to the shopping cart.")

    @Parameter(title: "Item", description: "The product to add")
    var item: ProductEntity

    @Parameter(title: "Quantity", description: "How many to add", default: 1)
    var quantity: Int

    func perform() async throws -> some IntentResult {
        try await Cart.shared.add(item, quantity: quantity)
        return .result()
    }
}
```

For each app intent you promote to a tool, help Siri’s model understand what the tool is and how it works by adding the following metadata:

- A `title` property that explains what the action is
- A `description` property that explains what the action does
- A title and description in each parameter’s `@Parameter` attribute that explain the parameter’s role in the action

Write each description for someone who doesn’t know your app, and include helpful or important details about a parameter’s value, such as:

- The format of a string
- The range of a floating-point number
- The units of an integer

> **Note**: Some of your app’s intents may already have this metadata if they appear in App Shortcuts, Spotlight, or the Shortcuts app.

A tool parameter can be a plain value type or a more complex type, such as one of your app’s [`AppEntity`](./appentity.md) types. For example, the `item` parameter of `AddToCart` is a `ProductEntity`, which is a type the app defines and implements. Siri finds a product for that parameter by running the entity’s query.

Consider making a [`TransientAppEntity`](./transientappentity.md) type generable by conforming it to [`GenerableEntity`](./generableentity.md) when:

- The type is a parameter type for a tool
- The model can configure all of the entity’s properties directly from the context of a person’s request, without looking anything up

An app intent that conforms to a schema can also be a tool. Add the [`tool`](./appintenttraits/tool.md) trait to the intent’s existing macro:

```swift
@AppIntent(.tool, schema: .books.openBook)
struct OpenBookIntent: OpenIntent {
    // A book the action navigates to in the reading app.
    var target: BookEntity

    func perform() async throws -> some IntentResult {
        // ...
    }
}
```

This combination works only for a schema that’s available exclusively in the Shortcuts app, such as `openBook`.

> ❗ **Important**: Adding the trait to an intent that conforms to a schema Siri already supports, such as [`sendMessage`](./appschema/messagesintent/sendmessage.md), is a build error.

For more information about schemas and the domains Siri supports, see [App schema domains](./app-schema-domains.md).

## Relationships

### Inherits From
- [AppIntent](./appintent.md)
- [PersistentlyIdentifiable](./persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tool support
- [macro AppIntent(AppIntentTraits)](./appintent%28_%29.md)
  Makes an existing app intent available to Siri as a tool.
- [macro AppIntent<T>(AppIntentTraits, schema: T)](./appintent%28_,schema%29.md)
  Makes an app intent that conforms to a schema available to Siri as a tool.
- [struct AppIntentTraits](./appintenttraits.md)
  The roles an app intent takes on, passed to `@AppIntent`.
- [struct IntentVisibility](./intentvisibility.md)
  A value that configures how a property is available to system features, such as Siri and Shortcuts, if at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/toolintent)*