# dropInteraction(_:sessionDidExit:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the drop session has moved out of the drop interaction’s view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, sessionDidExit session: any UIDropSession)
```

```objc
- (void) dropInteraction:(UIDropInteraction *) interaction sessionDidExit:(id<UIDropSession>) session;
```

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drop session that has moved out of the interaction’s view.

## See Also

### Tracking the drop movements
- [func dropInteraction(UIDropInteraction, sessionDidEnter: any UIDropSession)](./dropinteraction%28_,sessiondidenter%29.md)
  Tells the delegate the drop session has moved into the drop interaction’s view.
- [func dropInteraction(UIDropInteraction, sessionDidUpdate: any UIDropSession) -> UIDropProposal](./dropinteraction%28_,sessiondidupdate%29.md)
  Tells the delegate the drop session has changed.
- [func dropInteraction(UIDropInteraction, sessionDidEnd: any UIDropSession)](./dropinteraction%28_,sessiondidend%29.md)
  Tells the delegate the drop session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidexit:))*