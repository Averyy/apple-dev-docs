# init(forOpeningContentTypes:asCopy:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a document picker that can open or copy the types of documents you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
init(forOpeningContentTypes contentTypes: [UTType], asCopy: Bool)
```

```objc
- (instancetype) initForOpeningContentTypes:(NSArray<UTType *> *) contentTypes asCopy:(BOOL) asCopy;
```

## Parameters

- `contentTypes`: An array of uniform type identifiers for the document picker to display. For more information, see [Uniform Type Identifiers](../../UniformTypeIdentifiers/UniformTypeIdentifiers.md).
- `asCopy`: A Boolean value that indicates whether the document picker copies the selected document.

## See Also

### Creating a document picker
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns an initialized object from data in a specified unarchiver.
- [convenience init(forExporting: [URL])](./init%28forexporting%29.md)
  Creates and returns a document picker that can export the types of documents you specify.
- [init(forExporting: [URL], asCopy: Bool)](./init%28forexporting,ascopy%29.md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](./init%28foropeningcontenttypes%29.md)
  Creates and returns a document picker that can open the types of documents you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(foropeningcontenttypes:ascopy:))*