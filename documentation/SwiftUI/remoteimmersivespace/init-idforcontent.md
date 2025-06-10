# init(id:for:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates the remote immersive space associated with an identifier for a specified type of presented data.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init<C>(id: String, for type: Data.Type, @CompositorContentBuilder content: @escaping (Binding<Data?>) -> C) where Content == CompositorContentBuilder.Content<C>, C : CompositorContent
```

#### Discussion

The space uses the specified content builder to form the content. Your app invokes this initializer when it presents a value of the specified `type` using the [`openImmersiveSpace`](environmentvalues/openimmersivespace.md) action.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure   that identifiers are unique among the immersive spaces in your app.
- `type`: The type of presented data this immersive space accepts.
- `content`: A compositor content builder that defines the content   for each instance of the immersive space. The closure receives a   binding to the value that you pass to the    action when you call that   action to open an immersive space. The system automatically persists   and restores the value of this binding during state restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/remoteimmersivespace/init(id:for:content:))*