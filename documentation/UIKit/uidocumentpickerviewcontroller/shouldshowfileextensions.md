# shouldShowFileExtensions

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the browser always shows file extensions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldShowFileExtensions: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  This property has no effect in Mac apps built with Mac Catalyst.

## See Also

- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerviewcontroller/documentpickermode.md)
  The type of file transfer operation that the document picker uses.
- [enum UIDocumentPickerMode](uidocumentpickermode.md)
  Modes that define the type of file transfer operation that the document picker uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/shouldshowfileextensions)*