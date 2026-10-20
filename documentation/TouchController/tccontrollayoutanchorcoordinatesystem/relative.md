# TCControlLayoutAnchorCoordinateSystem.relative

**Framework**: Touch Controller  
**Kind**: case  
**Role**: Case

Anchors are positioned relative to the device’s screen size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case relative
```

```c
TCControlLayoutAnchorCoordinateSystemRelative
```

#### Discussion

- On larger devices, the coordinate system is shrunk for easier handling.
- On smaller devices, this is equivalent to `TCControlLayoutAnchorCoordinateSystemAbsolute`.

## See Also

### Anchors
- [TCControlLayoutAnchorCoordinateSystem.absolute](./absolute.md)
  Anchors are positioned according to the absolute edges of the sceren.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollayoutanchorcoordinatesystem/relative)*