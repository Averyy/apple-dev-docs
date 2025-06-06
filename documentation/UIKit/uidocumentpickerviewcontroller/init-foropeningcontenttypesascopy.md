# init(forOpeningContentTypes:asCopy:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a document picker that can open or copy the types of documents you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(forOpeningContentTypes contentTypes: [UTType], asCopy: Bool)
```

## Parameters

- `contentTypes`: An array of uniform type identifiers for the document picker to display. For more information, see  .
- `asCopy`: A Boolean value that indicates whether the document picker copies the selected document.

## See Also

- [init?(coder: NSCoder)](uidocumentpickerviewcontroller/init(coder:).md)
  Returns an initialized object from data in a specified unarchiver.
- [convenience init(forExporting: [URL])](uidocumentpickerviewcontroller/init(forexporting:).md)
  Creates and returns a document picker that can export the types of documents you specify.
- [init(forExporting: [URL], asCopy: Bool)](uidocumentpickerviewcontroller/init(forexporting:ascopy:).md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](uidocumentpickerviewcontroller/init(foropeningcontenttypes:).md)
  Creates and returns a document picker that can open the types of documents you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(foropeningcontenttypes:ascopy:))*