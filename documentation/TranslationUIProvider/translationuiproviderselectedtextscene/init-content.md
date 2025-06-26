# init(content:)

**Framework**: TranslationUIProvider  
**Kind**: init

Creates the scene to translate the user’s selected text, with the provided View content.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
@MainActor
@preconcurrency init(content: @escaping (any TranslationUIProviderContext) -> Content)
```

## Parameters

- `content`: The content the framework should your to initialize the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationuiproviderselectedtextscene/init(content:))*