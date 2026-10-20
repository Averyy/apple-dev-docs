# TranslationUIProviderSelectedTextScene

**Framework**: TranslationUIProvider  
**Kind**: struct  
**Role**: Structure

The specific app extension scene that this extension provides.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
@preconcurrency struct TranslationUIProviderSelectedTextScene<Content> where Content : View
```

## Topics

### Initializers
- [init(content: (any TranslationUIProviderContext) -> Content)](./translationuiproviderselectedtextscene/init%28content%29.md)
  Creates the scene to translate the user’s selected text, with the provided View content.

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/appextensionscene.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TranslationUIProviderExtensionScene](./translationuiproviderextensionscene.md)

## See Also

### Configuration and text selection
- [struct TranslationProviderUIExtensionConfiguration](./translationprovideruiextensionconfiguration.md)
  The type for a translation UI provider extension’s configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationuiproviderselectedtextscene)*