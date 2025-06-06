# activeDocumentCreationIntent

**Framework**: UIKit  
**Kind**: property

The current intent that defines how your app creates a document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var activeDocumentCreationIntent: UIDocument.CreationIntent? { get }
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Discussion

Use this property to access the current intent. For more information, see [`Customizing a document-based app’s launch experience`](customizing-a-document-based-app-s-launch-experience.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/activedocumentcreationintent)*