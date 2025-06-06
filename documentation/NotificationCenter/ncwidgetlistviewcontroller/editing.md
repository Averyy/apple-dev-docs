# editing

**Framework**: Notification Center  
**Kind**: property

A Boolean value that indicates whether the list is in editing mode.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var editing: Bool { get set }
```

#### Discussion

When you set this property to [`true`](https://developer.apple.com/documentation/swift/true), the list view controller can display controls for reordering and removing rows. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var showsAddButtonWhenEditing: Bool](ncwidgetlistviewcontroller/showsaddbuttonwhenediting.md)
  A Boolean value that indicates whether an Add (+) button is displayed while the list is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/editing)*