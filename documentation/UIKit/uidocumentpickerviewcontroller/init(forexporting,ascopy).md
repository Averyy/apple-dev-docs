# init(forExporting:asCopy:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a document picker that can export or copy the types of documents you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
init(forExporting urls: [URL], asCopy: Bool)
```

```objc
- (instancetype) initForExportingURLs:(NSArray<NSURL *> *) urls asCopy:(BOOL) asCopy;
```

## Parameters

- `urls`: An array of documents that the document picker exports or copies.
- `asCopy`: A Boolean value that indicates whether the document picker copies the selected document.

## See Also

### Creating a document picker
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns an initialized object from data in a specified unarchiver.
- [convenience init(forExporting: [URL])](./init%28forexporting%29.md)
  Creates and returns a document picker that can export the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](./init%28foropeningcontenttypes%29.md)
  Creates and returns a document picker that can open the types of documents you specify.
- [init(forOpeningContentTypes: [UTType], asCopy: Bool)](./init%28foropeningcontenttypes,ascopy%29.md)
  Creates and returns a document picker that can open or copy the types of documents you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(forexporting:ascopy:))*