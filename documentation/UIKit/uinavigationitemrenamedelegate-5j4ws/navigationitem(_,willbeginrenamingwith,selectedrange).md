# navigationItem(_:willBeginRenamingWith:selectedRange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate when the rename process starts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func navigationItem(_: UINavigationItem, willBeginRenamingWith suggestedTitle: String, selectedRange: Range<String.Index>) -> (String, Range<String.Index>)
```

#### Return Value

A string that contains the initial text that appears in the rename text field, and a range that determines which part of that text has selection.

#### Discussion

UIKit calls this method when the rename process begins. Implement this method to customize the initial text and text selection that appears in the rename text field.

## Parameters

- `_`: The navigation item with the changing title.
- `suggestedTitle`: The initial text to appear in the rename text field.
- `selectedRange`: The selected range of the initial text in the rename text field.

## Default Implementations

### UINavigationItemRenameDelegate Implementations
- [func navigationItem(UINavigationItem, willBeginRenamingWith: String, selectedRange: Range<String.Index>) -> (String, Range<String.Index>)](./navigationitem%28_,willbeginrenamingwith,selectedrange%29-396y6.md)

## See Also

### Handling the rename process
- [func navigationItem(UINavigationItem, didEndRenamingWith: String)](./navigationitem%28_,didendrenamingwith%29.md)
  Tells the delegate when the rename process ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:willbeginrenamingwith:selectedrange:))*