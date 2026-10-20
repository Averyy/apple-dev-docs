# regionOfInterest

**Framework**: DockKit  
**Kind**: property  
**Role**: Instance Property

The area in the video frame in which the dock accessory tracks a subject.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final var regionOfInterest: CGRect { get }
```

## See Also

### Performing animation
- [func animate(motion: DockAccessory.Animation) async throws -> Progress](./animate%28motion%29.md)
  Starts an animation sequence.
- [func setRegionOfInterest(CGRect) async throws](./setregionofinterest%28_%29.md)
  Sets the area in the video frame in which the dock accessory tracks a subject.
- [DockAccessory.Animation](./animation.md)
  Character animations that describe how to move the dock accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/regionofinterest)*