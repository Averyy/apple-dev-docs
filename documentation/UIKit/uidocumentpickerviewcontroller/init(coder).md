# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized object from data in a specified unarchiver.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: An unarchiver object.

## See Also

### Creating a document picker
- [convenience init(forExporting: [URL])](./init%28forexporting%29.md)
  Creates and returns a document picker that can export the types of documents you specify.
- [init(forExporting: [URL], asCopy: Bool)](./init%28forexporting,ascopy%29.md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](./init%28foropeningcontenttypes%29.md)
  Creates and returns a document picker that can open the types of documents you specify.
- [init(forOpeningContentTypes: [UTType], asCopy: Bool)](./init%28foropeningcontenttypes,ascopy%29.md)
  Creates and returns a document picker that can open or copy the types of documents you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(coder:))*