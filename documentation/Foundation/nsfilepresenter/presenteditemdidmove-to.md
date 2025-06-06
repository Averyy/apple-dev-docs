# presentedItemDidMove(to:)

**Framework**: Foundation  
**Kind**: method

Tells your object that the presented item moved or was renamed.

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
optional func presentedItemDidMove(to newURL: URL)
```

#### Discussion

Use this method to update the value returned by the [`presentedItemURL`](nsfilepresenter/presenteditemurl.md) property of your object.

## Parameters

- `newURL`: The URL containing the new path to the presented item.

## See Also

- [var presentedItemURL: URL?](nsfilepresenter/presenteditemurl.md)
  The URL of the presented file or directory.
- [func savePresentedItemChanges(completionHandler: ((any Error)?) -> Void)](nsfilepresenter/savepresenteditemchanges(completionhandler:).md)
  Tells your object to save any unsaved changes for the presented item.
- [func accommodatePresentedItemDeletion(completionHandler: ((any Error)?) -> Void)](nsfilepresenter/accommodatepresenteditemdeletion(completionhandler:).md)
  Tells your object that its presented item is about to be deleted.
- [func presentedItemDidChange()](nsfilepresenter/presenteditemdidchange.md)
  Tells your object that the presented item’s contents or attributes changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidmove(to:))*