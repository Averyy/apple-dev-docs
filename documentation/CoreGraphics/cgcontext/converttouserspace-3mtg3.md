# convertToUserSpace(_:)

**Framework**: Core Graphics  
**Kind**: method

Returns a point that is transformed from device space coordinates to user space coordinates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func convertToUserSpace(_ point: CGPoint) -> CGPoint
```

#### Return Value

The coordinates of the point in user space coordinates.

## Parameters

- `point`: The point, in device space coordinates, to transform.

## See Also

- [var userSpaceToDeviceSpaceTransform: CGAffineTransform](cgcontext/userspacetodevicespacetransform.md)
  Returns an affine transform that maps user space coordinates to device space coordinates.
- [func convertToDeviceSpace(CGPoint) -> CGPoint](cgcontext/converttodevicespace(_:)-53m7u.md)
  Returns a point that is transformed from user space coordinates to device space coordinates.
- [func convertToDeviceSpace(CGRect) -> CGRect](cgcontext/converttodevicespace(_:)-91x5g.md)
  Returns a rectangle that is transformed from user space coordinate to device space coordinates.
- [func convertToUserSpace(CGRect) -> CGRect](cgcontext/converttouserspace(_:)-1hk5r.md)
  Returns a rectangle that is transformed from device space coordinate to user space coordinates.
- [func convertToDeviceSpace(CGSize) -> CGSize](cgcontext/converttodevicespace(_:)-224h2.md)
  Returns a size that is transformed from user space coordinates to device space coordinates.
- [func convertToUserSpace(CGSize) -> CGSize](cgcontext/converttouserspace(_:)-693ur.md)
  Returns a size that is transformed from device space coordinates to user space coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/converttouserspace(_:)-3mtg3)*