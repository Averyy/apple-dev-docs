# init(forExporting:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a document picker that can export the types of documents you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(forExporting urls: [URL])
```

```objc
- (instancetype) initForExportingURLs:(NSArray<NSURL *> *) urls;
```

## Parameters

- `urls`: An array of documents that the document picker exports.

## See Also

### Creating a document picker
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns an initialized object from data in a specified unarchiver.
- [init(forExporting: [URL], asCopy: Bool)](./init%28forexporting,ascopy%29.md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](./init%28foropeningcontenttypes%29.md)
  Creates and returns a document picker that can open the types of documents you specify.
- [init(forOpeningContentTypes: [UTType], asCopy: Bool)](./init%28foropeningcontenttypes,ascopy%29.md)
  Creates and returns a document picker that can open or copy the types of documents you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(forexporting:))*