# init(source:)

**Framework**: SwiftUI  
**Kind**: init

Creates and opens new documents from a specified source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(source: NewDocumentButtonDataSource)
```

#### Discussion

The button creates new documents of the writable content types of all the document types supported by `DocumentGroup`s in the App definition. If a document type is not associated with any `DocumentGroup`, the button won’t create new documents of that type.

The framework watches for the relevant content types on the pasteboard. When there are no matching or conforming types, the button is disabled.

## Parameters

- `source`: A source of data that fills the newly created document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(source:))*