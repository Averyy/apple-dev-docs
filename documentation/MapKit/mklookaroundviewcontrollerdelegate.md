# MKLookAroundViewControllerDelegate

**Framework**: MapKit  
**Kind**: protocol

Methods you implement to respond to changes in the LookAround view controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol MKLookAroundViewControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to scene changes
- [func lookAroundViewControllerWillUpdateScene(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillupdatescene(_:).md)
  Tells the delegate that the scene is about to update.
- [func lookAroundViewControllerDidUpdateScene(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdidupdatescene(_:).md)
  Tells the delegate that the scene updated.
### Entering and exiting full-screen modes
- [func lookAroundViewControllerWillPresentFullScreen(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillpresentfullscreen(_:).md)
  Tells the delegate when the view controller is about to enter full-screen mode.
- [func lookAroundViewControllerDidPresentFullScreen(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdidpresentfullscreen(_:).md)
  Tells the delegate when the view controller enters full-screen mode.
- [func lookAroundViewControllerWillDismissFullScreen(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwilldismissfullscreen(_:).md)
  Tells the delegate when the view controller is about to exit full-screen mode.
- [func lookAroundViewControllerDidDismissFullScreen(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdiddismissfullscreen(_:).md)
  Tells the delegate when the view controller exits full-screen mode.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any MKLookAroundViewControllerDelegate)?](mklookaroundviewcontroller/delegate.md)
  An object you provide to receive events related to the user’s interaction with the LookAround view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate)*