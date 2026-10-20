# userSpaceToDeviceSpaceTransform

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns an affine transform that maps user space coordinates to device space coordinates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userSpaceToDeviceSpaceTransform: CGAffineTransform { get }
```

```c
extern CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform(CGContextRef c);
```

## See Also

### Converting Between Coordinate Spaces
- [func convertToDeviceSpace(CGPoint) -> CGPoint](./converttodevicespace%28_%29-53m7u.md)
  Returns a point that is transformed from user space coordinates to device space coordinates.
- [func convertToUserSpace(CGPoint) -> CGPoint](./converttouserspace%28_%29-3mtg3.md)
  Returns a point that is transformed from device space coordinates to user space coordinates.
- [func convertToDeviceSpace(CGRect) -> CGRect](./converttodevicespace%28_%29-91x5g.md)
  Returns a rectangle that is transformed from user space coordinate to device space coordinates.
- [func convertToUserSpace(CGRect) -> CGRect](./converttouserspace%28_%29-1hk5r.md)
  Returns a rectangle that is transformed from device space coordinate to user space coordinates.
- [func convertToDeviceSpace(CGSize) -> CGSize](./converttodevicespace%28_%29-224h2.md)
  Returns a size that is transformed from user space coordinates to device space coordinates.
- [func convertToUserSpace(CGSize) -> CGSize](./converttouserspace%28_%29-693ur.md)
  Returns a size that is transformed from device space coordinates to user space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/userspacetodevicespacetransform)*