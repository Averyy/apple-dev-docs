# changeCount

**Framework**: UIKit  
**Kind**: property

The number of times the pasteboard’s contents change.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var changeCount: Int { get }
```

#### Discussion

Whenever the contents of a pasteboard changes—specifically, when pasteboard items are added, modified, or removed—`UIPasteboard` increments the value of this property. After it increments the change count, UIPasteboard posts the notifications named [`changedNotification`](uipasteboard/changednotification.md) (for additions and modifications) and [`removedNotification`](uipasteboard/removednotification.md) (for removals). These notifications include (in the `userInfo` dictionary) the types of the pasteboard items added or removed. Because `UIPasteboard` waits until the end of the current event loop before incrementing the change count, notifications can be batched. The class also updates the change count when an app reactivates and another app has changed the pasteboard contents. When users restart a device, the change count is reset to zero.

## See Also

- [var name: UIPasteboard.Name](uipasteboard/name-swift.property.md)
  The name of the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/changecount)*