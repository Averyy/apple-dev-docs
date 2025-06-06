# presentedSubitemDidChange(at:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the contents or attributes of the specified item changed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func presentedSubitemDidChange(at url: URL)
```

#### Discussion

This method is relevant for applications that present directories. This might occur if the delegate manages the contents of a directory or manages a file that is implemented as a file package. Your implementation of this method should take whatever actions necessary to handle the change in content or attributes of the specified item.

If the presented directory is a file package, the system calls the [`presentedItemDidChange()`](nsfilepresenter/presenteditemdidchange().md) method if your delegate does not implement this method.

## Parameters

- `url`: The URL of the item in the presented directory that changed. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

## See Also

- [func accommodatePresentedSubitemDeletion(at: URL, completionHandler: ((any Error)?) -> Void)](nsfilepresenter/accommodatepresentedsubitemdeletion(at:completionhandler:).md)
  Tells the delegate that some entity wants to delete an item that is inside of a presented directory.
- [func presentedSubitemDidAppear(at: URL)](nsfilepresenter/presentedsubitemdidappear(at:).md)
  Tells the delegate that an item was added to the presented directory.
- [func presentedSubitem(at: URL, didMoveTo: URL)](nsfilepresenter/presentedsubitem(at:didmoveto:).md)
  Tells the delegate that an item in the presented directory moved to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitemdidchange(at:))*