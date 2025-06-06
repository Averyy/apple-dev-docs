# init(forExporting:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a document picker that can export the types of documents you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(forExporting urls: [URL])
```

## Parameters

- `urls`: An array of documents that the document picker exports.

## See Also

- [init?(coder: NSCoder)](uidocumentpickerviewcontroller/init(coder:).md)
  Returns an initialized object from data in a specified unarchiver.
- [init(forExporting: [URL], asCopy: Bool)](uidocumentpickerviewcontroller/init(forexporting:ascopy:).md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](uidocumentpickerviewcontroller/init(foropeningcontenttypes:).md)
  Creates and returns a document picker that can open the types of documents you specify.
- [init(forOpeningContentTypes: [UTType], asCopy: Bool)](uidocumentpickerviewcontroller/init(foropeningcontenttypes:ascopy:).md)
  Creates and returns a document picker that can open or copy the types of documents you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(forexporting:))*