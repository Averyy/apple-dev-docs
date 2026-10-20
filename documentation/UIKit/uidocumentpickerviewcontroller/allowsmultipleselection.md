# allowsMultipleSelection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the user can select more than one document at a time.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsMultipleSelection: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsMultipleSelection;
```

#### Discussion

By default, this property is [`false`](../../Swift/false.md).

## See Also

### Getting the user-selected document
- [var delegate: (any UIDocumentPickerDelegate)?](./delegate.md)
  An object that acts as the delegate of the view controller.
- [protocol UIDocumentPickerDelegate](../uidocumentpickerdelegate.md)
  A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [var directoryURL: URL?](./directoryurl.md)
  The initial directory that the document picker displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/allowsmultipleselection)*