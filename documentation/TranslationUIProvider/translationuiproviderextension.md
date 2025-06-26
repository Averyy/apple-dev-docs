# TranslationUIProviderExtension

**Framework**: TranslationUIProvider  
**Kind**: protocol

A protocol that translation apps implement to provide a text-selection view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
protocol TranslationUIProviderExtension : AppExtension
```

## Topics

### Associated Types
- [associatedtype Body : TranslationUIProviderExtensionScene](translationuiproviderextension/body-swift.associatedtype.md)
  The type for this UI providers extensions’s body
### Instance Properties
- [var body: Self.Body](translationuiproviderextension/body-swift.property.md)
  The content and behavior of the UI provider extensions’s interface.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [protocol TranslationUIProviderContext](translationuiprovidercontext.md)
  An object that encapsulates the XPC communication between the host process and the third-party extension implementation.
- [protocol TranslationUIProviderExtensionScene](translationuiproviderextensionscene.md)
  The protocol this extension’s scene need to implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationuiproviderextension)*