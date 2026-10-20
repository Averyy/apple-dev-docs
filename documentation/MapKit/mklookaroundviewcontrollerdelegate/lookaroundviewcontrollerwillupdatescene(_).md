# lookAroundViewControllerWillUpdateScene(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the scene is about to update.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func lookAroundViewControllerWillUpdateScene(_ viewController: MKLookAroundViewController)
```

```objc
- (void) lookAroundViewControllerWillUpdateScene:(MKLookAroundViewController *) viewController;
```

## Parameters

- `viewController`: The [`MKLookAroundViewController`](../mklookaroundviewcontroller.md).

## See Also

### Responding to scene changes
- [func lookAroundViewControllerDidUpdateScene(MKLookAroundViewController)](./lookaroundviewcontrollerdidupdatescene%28_%29.md)
  Tells the delegate that the scene updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerwillupdatescene(_:))*