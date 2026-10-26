# navigationItem:didEndRenamingWithTitle:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the rename process ends.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) navigationItem:(UINavigationItem *) navigationItem didEndRenamingWithTitle:(NSString *) title;
```

#### Discussion

UIKit calls this method after a person finishes renaming the navigation item. Implement this method to update your data model with the new title as needed.

UIKit updates the navigation item’s title automatically. However, if you want to modify the final title that the system passes in to this method, you must update the navigation item’s title manually.

## Parameters

- `navigationItem`: The navigation item with the changing title.
- `title`: The new title of the navigation item.

## See Also

### Handling the rename process
- [- navigationItem:willBeginRenamingWithSuggestedTitle:selectedRange:](./navigationitem_willbeginrenamingwithsuggestedtitle_selectedrange_.md)
  Tells the delegate when the rename process starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:didendrenamingwithtitle:)*