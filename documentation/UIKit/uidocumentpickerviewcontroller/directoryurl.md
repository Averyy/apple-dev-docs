# directoryURL

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The initial directory that the document picker displays.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var directoryURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * directoryURL;
```

## Mentions

- [Providing access to directories](../providing-access-to-directories.md)

## Discussion

Set this property to specify the starting directory for the document picker. This property defaults to `nil`. If you specify a value, the document picker tries to start at the specified directory. Otherwise, it starts with the last directory chosen by the user.

The [`directoryURL`](./directoryurl.md) property only returns a value when you explicitly set it. For example, it doesn’t calculate the default URL presented to the user when the property isn’t set.

> **Note**:  This property has no effect in Mac apps built with Mac Catalyst.

## See Also

### Getting the user-selected document
- [var delegate: (any UIDocumentPickerDelegate)?](./delegate.md)
  An object that acts as the delegate of the view controller.
- [protocol UIDocumentPickerDelegate](../uidocumentpickerdelegate.md)
  A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that determines whether the user can select more than one document at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/directoryurl)*