# TCControlLayoutAnchorCoordinateSystem.relative

**Framework**: Touch Controller  
**Kind**: case

Anchors are positioned relative to the device’s screen size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case relative
```

#### Discussion

- On larger devices, the coordinate system is shrunk for easier handling.
- On smaller devices, this is equivalent to `TCControlLayoutAnchorCoordinateSystemAbsolute`.

## See Also

- [TCControlLayoutAnchorCoordinateSystem.absolute](tccontrollayoutanchorcoordinatesystem/absolute.md)
  Anchors are positioned according to the absolute edges of the sceren.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayoutanchorcoordinatesystem/relative)*