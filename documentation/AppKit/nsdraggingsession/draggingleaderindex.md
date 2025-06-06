# draggingLeaderIndex

**Framework**: AppKit  
**Kind**: property

The index of the dragging item under the cursor.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var draggingLeaderIndex: Int { get set }
```

#### Discussion

The index is to an element in the array passed as the first parameter to the [`NSView`](nsview.md) method [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md).

The default is the [`NSDraggingItem`](nsdraggingitem.md) closest to the `location` field in the event parameter that was passed to the [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsession/draggingleaderindex)*