# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a remote immersive space.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init<C>(@CompositorContentBuilder content: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `content`: A compositor content builder that defines the content   of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/remoteimmersivespace/init(content:))*