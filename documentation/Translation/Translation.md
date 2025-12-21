# Translation

**Framework**: Translation  
**Kind**: module

Translate text in your app from one language to another.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+

#### Overview

Offer in-app translations with the Translation framework. You can use the built-in UI and let the system offer a translation to users on your behalf. Or you can use the framework to customize the translation experience.

![A conceptual image showing a translation.](https://docs-assets.developer.apple.com/published/ba8981fe7411311080007ce755c7c010/hero%402x.png)

To offer the built-in system translation experience, anchor the [`translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)`](https://developer.apple.com/documentation/SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)) view modifier to the SwiftUI view containing the text to translate. Set `isPresented` to true when you want to the built-in system translation UI to appear. Pass the text to translate to the `text` parameter.

To customize the translation experience use one of the translation tasks such as [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)). These functions provides you with a  [`TranslationSession`](translationsession.md) that you can use to translate strings of text one at a time, or in a batch. You can check language availability before offering a translation with the [`LanguageAvailability`](languageavailability.md) class.

## Topics

### Essentials
- [Translating text within your app](translating-text-within-your-app.md)
  Display simple system translations and create custom translation experiences.
- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](../SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:).md)
  Presents a translation popover when a given condition is true.
- [func translationTask(TranslationSession.Configuration?, action: (TranslationSession) async -> Void) -> some View](../SwiftUI/View/translationTask(_:action:).md)
  Adds a task to perform before this view appears or when the translation configuration changes.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](../SwiftUI/View/translationTask(source:target:action:).md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
- [class TranslationSession](translationsession.md)
  A class that performs translations between a pair of languages.
### Availability
- [class LanguageAvailability](languageavailability.md)
  A check for language support and status.
### Errors
- [struct TranslationError](translationerror.md)
  Error codes describing why the framework can’t perform a translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Translation)*