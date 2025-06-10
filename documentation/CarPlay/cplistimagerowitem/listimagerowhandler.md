# listImageRowHandler

**Framework**: CarPlay  
**Kind**: property

An optional closure that CarPlay invokes when the user selects an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var listImageRowHandler: ((CPListImageRowItem, Int, @escaping () -> Void) -> Void)? { get set }
```

#### Discussion

In Swift, this property is a closure that has three parameters:

- The list item that contains the image.
- The selected image’s index in the list item’s image row.
- The completion closure you call to notify CarPlay when you finish processing the selection.

In Objective-C, the block’s parameters are:

CarPlay executes your handler on the main queue. You must call the completion closure, or `completionBlock` in Objective-C, after you finish processing the selection. If you need to perform asynchronous tasks, dispatch them to a background queue and call the completion closure or `completionBlock` when they complete. CarPlay displays an asynchronous progress indicator until you call the completion closure.

## See Also

- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](cplistimagerowitem/handler.md)
  An optional closure that CarPlay invokes when the user selects the list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/listimagerowhandler)*