# deletePlaceholder()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes an unneeded placeholder cell altogether from the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func deletePlaceholder() -> Bool
```

```objc
- (BOOL) deletePlaceholder;
```

#### Return Value

[`true`](../../Swift/true.md) if the placeholder cell was removed, or [`false`](../../Swift/false.md) if the cell was no longer in the collection view.

#### Discussion

Use this method to remove a placeholder cell without swapping in a new cell. You might call this method if the user chooses to undo the insertion of a cell or if the contents of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholdercontext/deleteplaceholder())*