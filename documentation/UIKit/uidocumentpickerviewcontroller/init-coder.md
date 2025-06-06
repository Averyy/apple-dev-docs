# init(coder:)

**Framework**: UIKit  
**Kind**: init

Returns an initialized object from data in a specified unarchiver.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

## Parameters

- `coder`: An unarchiver object.

## See Also

- [convenience init(forExporting: [URL])](uidocumentpickerviewcontroller/init(forexporting:).md)
  Creates and returns a document picker that can export the types of documents you specify.
- [init(forExporting: [URL], asCopy: Bool)](uidocumentpickerviewcontroller/init(forexporting:ascopy:).md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](uidocumentpickerviewcontroller/init(foropeningcontenttypes:).md)
  Creates and returns a document picker that can open the types of documents you specify.
- [init(forOpeningContentTypes: [UTType], asCopy: Bool)](uidocumentpickerviewcontroller/init(foropeningcontenttypes:ascopy:).md)
  Creates and returns a document picker that can open or copy the types of documents you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(coder:))*