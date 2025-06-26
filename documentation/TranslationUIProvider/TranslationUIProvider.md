# TranslationUIProvider

**Framework**: TranslationUIProvider  
**Kind**: module

Provide UI for translations of text people select.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Topics

### Essentials
- [Preparing your app to be the default translation app](preparing-your-app-to-be-the-default-translation-app.md)
  Configure your app so people can set it as the default translation app on their device.
### Creating translation app extensions
- [protocol TranslationUIProviderContext](translationuiprovidercontext.md)
  An object that encapsulates the XPC communication between the host process and the third-party extension implementation.
- [protocol TranslationUIProviderExtension](translationuiproviderextension.md)
  A protocol that translation apps implement to provide a text-selection view.
- [protocol TranslationUIProviderExtensionScene](translationuiproviderextensionscene.md)
  The protocol this extension’s scene need to implement.
### Configuration and text selection
- [struct TranslationProviderUIExtensionConfiguration](translationprovideruiextensionconfiguration.md)
  The type for a translation UI provider extension’s configuration object.
- [struct TranslationUIProviderSelectedTextScene](translationuiproviderselectedtextscene.md)
  The specific app extension scene that this extension provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TranslationUIProvider)*