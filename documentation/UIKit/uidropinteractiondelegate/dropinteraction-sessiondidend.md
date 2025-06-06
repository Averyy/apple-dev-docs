# dropInteraction(_:sessionDidEnd:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate the drop session has ended.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dropInteraction(_ interaction: UIDropInteraction, sessionDidEnd session: any UIDropSession)
```

#### Discussion

Implement this method if you need to clean up resources you created during the session.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drop session that ended.

## See Also

- [func dropInteraction(UIDropInteraction, sessionDidEnter: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:sessiondidenter:).md)
  Tells the delegate the drop session has moved into the drop interaction’s view.
- [func dropInteraction(UIDropInteraction, sessionDidUpdate: any UIDropSession) -> UIDropProposal](uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:).md)
  Tells the delegate the drop session has changed.
- [func dropInteraction(UIDropInteraction, sessionDidExit: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:sessiondidexit:).md)
  Tells the delegate the drop session has moved out of the drop interaction’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidend:))*