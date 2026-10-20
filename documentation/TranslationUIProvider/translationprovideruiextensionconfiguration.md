# TranslationProviderUIExtensionConfiguration

**Framework**: TranslationUIProvider  
**Kind**: struct  
**Role**: Structure

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
- [init(any TranslationUIProviderExtension)](./translationprovideruiextensionconfiguration/init%28_%29.md)
  Creates a default configuration for the given extension.

## Relationships

### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/appextensionconfiguration.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuration and text selection
- [struct TranslationUIProviderSelectedTextScene](./translationuiproviderselectedtextscene.md)
  The specific app extension scene that this extension provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationprovideruiextensionconfiguration)*