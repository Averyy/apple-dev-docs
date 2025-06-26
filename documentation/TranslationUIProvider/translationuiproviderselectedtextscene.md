# TranslationUIProviderSelectedTextScene

**Framework**: TranslationUIProvider  
**Kind**: struct

The specific app extension scene that this extension provides.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
@MainActor
@preconcurrency struct TranslationUIProviderSelectedTextScene<Content> where Content : View
```

## Topics

### Initializers
- [init(content: (any TranslationUIProviderContext) -> Content)](translationuiproviderselectedtextscene/init(content:).md)
  Creates the scene to translate the user’s selected text, with the provided View content.
### Instance Properties
- [var body: some AppExtensionScene](translationuiproviderselectedtextscene/body-swift.property.md)
  The content and behavior of the scene’s user interface.
### Type Aliases
- [TranslationUIProviderSelectedTextScene.Body](translationuiproviderselectedtextscene/body-swift.typealias.md)
  The type for this scene’s body.

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TranslationUIProviderExtensionScene](translationuiproviderextensionscene.md)

## See Also

- [struct TranslationProviderUIExtensionConfiguration](translationprovideruiextensionconfiguration.md)
  The type for a translation UI provider extension’s configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationuiproviderselectedtextscene)*