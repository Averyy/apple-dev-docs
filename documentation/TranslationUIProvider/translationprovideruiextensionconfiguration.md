# TranslationProviderUIExtensionConfiguration

**Framework**: TranslationUIProvider  
**Kind**: struct

The type for a translation UI provider extension’s configuration object.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
@preconcurrency struct TranslationProviderUIExtensionConfiguration
```

## Topics

### Creating a configuration
- [init(any TranslationUIProviderExtension)](translationprovideruiextensionconfiguration/init(_:).md)
  Creates a default configuration for the given extension.

## Relationships

### Conforms To
- [AppExtensionConfiguration](../extensionfoundation/appextensionconfiguration.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct TranslationUIProviderSelectedTextScene](translationuiproviderselectedtextscene.md)
  The specific app extension scene that this extension provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationprovideruiextensionconfiguration)*