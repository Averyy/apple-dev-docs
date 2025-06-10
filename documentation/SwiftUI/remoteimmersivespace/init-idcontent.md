# init(id:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates the remote immersive space associated with the specified identifier.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init<C>(id: String, @CompositorContentBuilder content: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure   that identifiers are unique among the immersive spaces in your app.
- `content`: An compositor content builder that defines the content   of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/remoteimmersivespace/init(id:content:))*