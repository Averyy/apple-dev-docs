# TranslationUIProviderContext

**Framework**: TranslationUIProvider  
**Kind**: protocol  
**Role**: Protocol

An object that encapsulates the XPC communication between the host process and the third-party extension implementation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
protocol TranslationUIProviderContext : Observable
```

## Discussion

The framework provides information to the extension through the two observable properties [`inputText`](./translationuiprovidercontext/inputtext.md) and [`allowsReplacement`](./translationuiprovidercontext/allowsreplacement.md), and the extension calls back to the host process using the functions [`finish(translation:)`](./translationuiprovidercontext/finish%28translation%29.md) and, optionally [`expandSheet()`](./translationuiprovidercontext/expandsheet%28%29.md).

## Topics

### Instance Properties
- [var allowsReplacement: Bool](./translationuiprovidercontext/allowsreplacement.md)
  A Boolean value that indicates whether the control can replace the source text.
- [var inputText: AttributedString?](./translationuiprovidercontext/inputtext.md)
  The source text to translate.
### Instance Methods
- [func expandSheet()](./translationuiprovidercontext/expandsheet%28%29.md)
  The framework requests that the sheet expand.
- [func finish(translation: AttributedString?)](./translationuiprovidercontext/finish%28translation%29.md)
  Completes the translation after which the framework closes the sheet.

## Relationships

### Inherits From
- [Observable](../Observation/observable.md)

## See Also

### Creating translation app extensions
- [protocol TranslationUIProviderExtension](./translationuiproviderextension.md)
  A protocol that translation apps implement to provide a text-selection view.
- [protocol TranslationUIProviderExtensionScene](./translationuiproviderextensionscene.md)
  The protocol this extension’s scene need to implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationuiprovidercontext)*