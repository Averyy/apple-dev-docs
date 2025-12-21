# allowsMoveOperation

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the drag session permits moving drag items within the same app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsMoveOperation: Bool { get }
```

#### Discussion

A move operation can be applied only within the same app. Drag items shared with another app are always copied.

The `allowsMoveOperation` value is determined by the return value of the source app’s drag interaction delegate’s  [`dragInteraction(_:sessionAllowsMoveOperation:)`](uidraginteractiondelegate/draginteraction(_:sessionallowsmoveoperation:).md) method. If `allowsMoveOperation` is [`true`](https://developer.apple.com/documentation/Swift/true), the source app’s drop interaction delegate’s [`dropInteraction(_:sessionDidUpdate:)`](uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:).md) method can return a drop proposal for a [`UIDropOperation.move`](uidropoperation/move.md) operation.

## See Also

- [var isRestrictedToDraggingApplication: Bool](uidragdropsession/isrestrictedtodraggingapplication.md)
  A Boolean value that indicates whether the drag session is confined to the app that started the drag activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/allowsmoveoperation)*