# init(supportedFamilies:content:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates a card snippet with the views for specific families of content.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
init(supportedFamilies: [CardSnippetFamily], @ViewBuilder content: @escaping @MainActor (Entity, CardSnippetContext) -> Content)
```

## Discussion

The builder can adapt the layout based on the rendering family from the card snippet context.

```swift
CardSnippet(supportedFamilies: [.standard]) { recipe, context in
   switch context.family {
       case .standard:
            LargeRecipeCardView(recipe: recipe)
        default:
            RecipeCardView(recipe: recipe)
    }
}
```

Use this initializer to deliver a SwiftUI view with the visual representation of your entity. Create your view primarily with static content such as text and images. The system renders snippets in advance and stores your views in a static archive it can use at any time, including when your app isn’t running, so you can’t change the content of your view later. If your view requires data that isn’t immediately available, prepare the data before you return the SwiftUI view from your closure. For example, if you need to create custom images, create them before you return your view. Prepare data synchronously to ensure it’s available when you create your view. If you generate data asynchronously, it likely won’t be available in time.

## Parameters

- `supportedFamilies`: The families the card supports. Each family represents the intended context and amount of space available for your custom views. For example, specify[`standard`](../cardsnippetfamily/standard.md) if your views are suitable for display on iPhone. If you don’t support the family the system needs, the system presents your entity using content from its display representation instead.
- `content`: The view builder to create your view. The closure for the view builder takes the following parameters:

  - **`entity`**: An instance of your [`AppEntity`](../appentity.md) type.
  - **`context`**: A [`CardSnippetContext`](../cardsnippetcontext.md) instance with information about the rendering environment. Combine the information in this instance with other SwiftUI environment variables to render your content. For example, get the current color scheme and locale from the SwiftUI environment values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cardsnippet/init(supportedfamilies:content:))*