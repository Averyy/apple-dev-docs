# presentedItemDidMove(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) presentedItemDidMoveToURL:(NSURL *) newURL;
```

## Discussion

Use this method to update the value returned by the [`presentedItemURL`](./presenteditemurl.md) property of your object.

## Parameters

- `newURL`: The URL containing the new path to the presented item.

## See Also

### Related Documentation
- [var presentedItemURL: URL?](./presenteditemurl.md)
  The URL of the presented file or directory.
### Handling Changes to Files
- [func savePresentedItemChanges(completionHandler: ((any Error)?) -> Void)](./savepresenteditemchanges%28completionhandler%29.md)
  Tells your object to save any unsaved changes for the presented item.
- [func accommodatePresentedItemDeletion(completionHandler: ((any Error)?) -> Void)](./accommodatepresenteditemdeletion%28completionhandler%29.md)
  Tells your object that its presented item is about to be deleted.
- [func presentedItemDidChange()](./presenteditemdidchange%28%29.md)
  Tells your object that the presented item’s contents or attributes changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidmove(to:))*