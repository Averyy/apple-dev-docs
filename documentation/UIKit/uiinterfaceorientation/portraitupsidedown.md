# UIInterfaceOrientation.portraitUpsideDown

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The device is in portrait mode but is upside down, with the device upright and the Home button at the top.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
case portraitUpsideDown
```

```c
UIInterfaceOrientationPortraitUpsideDown
```

#### Discussion

[`UIViewController`](../uiviewcontroller.md) doesn’t support this case on devices without a Home button.

## See Also

### Orientations
- [UIInterfaceOrientation.unknown](./unknown.md)
  The orientation of the device is unknown.
- [UIInterfaceOrientation.portrait](./portrait.md)
  The device is in portrait mode, with the device upright and the Home button on the bottom.
- [UIInterfaceOrientation.landscapeLeft](./landscapeleft.md)
  The device is in landscape mode, with the device upright and the Home button on the left.
- [UIInterfaceOrientation.landscapeRight](./landscaperight.md)
  The device is in landscape mode, with the device upright and the Home button on the right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterfaceorientation/portraitupsidedown)*