# init(_:contentType:)

**Framework**: SwiftUI  
**Kind**: init

Creates and opens new documents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, contentType: UTType? = nil)
```

## Parameters

- `title`: A title resource to use as the button title.
- `contentType`: An optional content type of the document to create.

## See Also

- [init(_:contentType:prepareDocumentURL:)](newdocumentbutton/init(_:contenttype:preparedocumenturl:).md)
  Creates and opens new documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:))*