# isRestrictedToDraggingApplication

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the drag session is confined to the app that started the drag activity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isRestrictedToDraggingApplication: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRestrictedToDraggingApplication) BOOL restrictedToDraggingApplication;
```

## Discussion

The value for this property is set by the source app’s drag interaction delegate method [`dragInteraction(_:sessionIsRestrictedToDraggingApplication:)`](../uidraginteractiondelegate/draginteraction%28_,sessionisrestrictedtodraggingapplication%29.md).  If the value is [`true`](../../Swift/true.md), the drag session is restricted to the app that started the drag operation.

## See Also

### Checking for drag and drop session restrictions
- [var allowsMoveOperation: Bool](./allowsmoveoperation.md)
  A Boolean value that indicates whether the drag session permits moving drag items within the same app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/isrestrictedtodraggingapplication)*