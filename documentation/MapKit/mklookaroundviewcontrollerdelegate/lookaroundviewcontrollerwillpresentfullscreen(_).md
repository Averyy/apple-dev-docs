# lookAroundViewControllerWillPresentFullScreen(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the view controller is about to enter full-screen mode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func lookAroundViewControllerWillPresentFullScreen(_ viewController: MKLookAroundViewController)
```

```objc
- (void) lookAroundViewControllerWillPresentFullScreen:(MKLookAroundViewController *) viewController;
```

## Parameters

- `viewController`: The [`MKLookAroundViewController`](../mklookaroundviewcontroller.md).

## See Also

### Entering and exiting full-screen modes
- [func lookAroundViewControllerDidPresentFullScreen(MKLookAroundViewController)](./lookaroundviewcontrollerdidpresentfullscreen%28_%29.md)
  Tells the delegate when the view controller enters full-screen mode.
- [func lookAroundViewControllerWillDismissFullScreen(MKLookAroundViewController)](./lookaroundviewcontrollerwilldismissfullscreen%28_%29.md)
  Tells the delegate when the view controller is about to exit full-screen mode.
- [func lookAroundViewControllerDidDismissFullScreen(MKLookAroundViewController)](./lookaroundviewcontrollerdiddismissfullscreen%28_%29.md)
  Tells the delegate when the view controller exits full-screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillpresentfullscreen(_:))*