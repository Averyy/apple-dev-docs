# snippet

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The snippet that contains the view to display.

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
@EntitySnippetContentBuilder
<Self> static var snippet: Self.Body { get }
```

## Discussion

Set the value of this property to a result builder that returns a [`CardSnippet`](../cardsnippet.md) type. Initialize the type with the SwiftUI view that displays the content from the provided entity. The following example shows an implementation of this property for an app entity that manages one of the app’s photos. The `PhotoCardView` is a custom SwiftUI view from the app that displays the provided entity and other relevant information.

```swift
extension PhotoEntity: SnippetRepresentableEntity {
    static var snippet: some EntitySnippetContent<Self> {
        CardSnippet(supportedFamilies: [.standard]) { photo, context in
            PhotoCardView(photo: photo)
        }
    }
}
```

If your view requires data that isn’t immediately available in your entity, prepare the data before you return the SwiftUI view from your snippet. For example, if you need to create custom images, create them before you return your view. Prepare data synchronously to ensure it’s available when you create your view. If you generate data asynchronously, it likely won’t be available in time.

## See Also

### Configuring the snippet
- [associatedtype Body : EntitySnippetContent](./body.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/snippetrepresentableentity/snippet)*