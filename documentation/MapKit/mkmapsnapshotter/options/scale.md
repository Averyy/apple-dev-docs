# scale

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The scale factor to use when creating the image.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS 9.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`traitCollection`](../snapshot/traitcollection.md) instead.

## Declaration

```swift
var scale: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat scale;
```

## Discussion

The value of this property is either `1.0` or `2.0`, depending on whether the device has a standard or Retina display. Set the value to `1.0` if you want to display the resulting image on a standard resolution display. Set the value to 2.0 if you want to display the image on a Retina display or want to use the image for printing.

This snapshotter sets this property to a default value that corresponds to the resolution of the current device’s display. You can change the value as needed to generate an image suitable for display on a different device.

## See Also

### Configuring the image output
- [var traitCollection: UITraitCollection](./traitcollection.md)
  Traits that determine the appearance of the map snapshot.
- [var size: CGSize](./size.md)
  The size of the image that you want to create.
- [var appearance: NSAppearance?](./appearance.md)
  The visual style (light or dark) to apply to the map when rendering the snapshot image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/scale)*