# delegate

**Framework**: MapKit  
**Kind**: property

An object you provide to receive events related to the user’s interaction with the LookAround view controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@IBOutlet
@MainActor weak var delegate: (any MKLookAroundViewControllerDelegate)? { get set }
```

## See Also

- [protocol MKLookAroundViewControllerDelegate](mklookaroundviewcontrollerdelegate.md)
  Methods you implement to respond to changes in the LookAround view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundviewcontroller/delegate)*