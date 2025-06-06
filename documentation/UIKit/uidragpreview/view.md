# view

**Framework**: UIKit  
**Kind**: property

The view associated with the drag item preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var view: UIView { get }
```

#### Discussion

The drag item preview uses the view to create a visual snapshot that’s displayed while the user drags the item across the screen. Changes you make to the view don’t appear in the preview after the snapshot is taken, and the preview doesn’t make changes or move the view. Any visual changes or movement made by the preview are applied to the snapshot only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreview/view)*