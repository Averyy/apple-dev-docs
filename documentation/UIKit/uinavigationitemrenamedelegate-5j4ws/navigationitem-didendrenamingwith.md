# navigationItem(_:didEndRenamingWith:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the delegate when the rename process ends.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func navigationItem(_: UINavigationItem, didEndRenamingWith title: String)
```

#### Discussion

UIKit calls this method after a person finishes renaming the navigation item. Implement this method to update your data model with the new title as needed.

UIKit updates the navigation item’s title automatically. However, if you want to modify the final title that the system passes in to this method, you must update the navigation item’s title manually.

## Parameters

- `title`: The new title of the navigation item.

## See Also

- [func navigationItem(UINavigationItem, willBeginRenamingWith: String, selectedRange: Range<String.Index>) -> (String, Range<String.Index>)](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:willbeginrenamingwith:selectedrange:).md)
  Tells the delegate when the rename process starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:))*