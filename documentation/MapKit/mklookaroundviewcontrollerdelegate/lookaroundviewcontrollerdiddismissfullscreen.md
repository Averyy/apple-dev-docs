# lookAroundViewControllerDidDismissFullScreen(_:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the view controller exits full-screen mode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func lookAroundViewControllerDidDismissFullScreen(_ viewController: MKLookAroundViewController)
```

## Parameters

- `viewController`: The  .

## See Also

- [func lookAroundViewControllerWillPresentFullScreen(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillpresentfullscreen(_:).md)
  Tells the delegate when the view controller is about to enter full-screen mode.
- [func lookAroundViewControllerDidPresentFullScreen(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdidpresentfullscreen(_:).md)
  Tells the delegate when the view controller enters full-screen mode.
- [func lookAroundViewControllerWillDismissFullScreen(MKLookAroundViewController)](mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwilldismissfullscreen(_:).md)
  Tells the delegate when the view controller is about to exit full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdiddismissfullscreen(_:))*