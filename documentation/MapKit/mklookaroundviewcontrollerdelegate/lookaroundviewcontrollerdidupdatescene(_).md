# lookAroundViewControllerDidUpdateScene(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the scene updated.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func lookAroundViewControllerDidUpdateScene(_ viewController: MKLookAroundViewController)
```

```objc
- (void) lookAroundViewControllerDidUpdateScene:(MKLookAroundViewController *) viewController;
```

## Parameters

- `viewController`: The [`MKLookAroundViewController`](../mklookaroundviewcontroller.md).

## See Also

### Responding to scene changes
- [func lookAroundViewControllerWillUpdateScene(MKLookAroundViewController)](./lookaroundviewcontrollerwillupdatescene%28_%29.md)
  Tells the delegate that the scene is about to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontrollerdelegate/lookaroundviewcontrollerdidupdatescene(_:))*