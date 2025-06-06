# isRestrictedToDraggingApplication

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the drag session is confined to the app that started the drag activity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isRestrictedToDraggingApplication: Bool { get }
```

#### Discussion

The value for this property is set by the source app’s drag interaction delegate method [`dragInteraction(_:sessionIsRestrictedToDraggingApplication:)`](uidraginteractiondelegate/draginteraction(_:sessionisrestrictedtodraggingapplication:).md).  If the value is [`true`](https://developer.apple.com/documentation/swift/true), the drag session is restricted to the app that started the drag operation.

## See Also

- [var allowsMoveOperation: Bool](uidragdropsession/allowsmoveoperation.md)
  A Boolean value that indicates whether the drag session permits moving drag items within the same app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/isrestrictedtodraggingapplication)*