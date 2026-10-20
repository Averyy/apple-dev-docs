# traitCollection

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

Traits that determine the appearance of the map snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var traitCollection: UITraitCollection { get set }
```

```objc
@property (nonatomic, copy) UITraitCollection * traitCollection;
```

## See Also

### Configuring the image output
- [var size: CGSize](./size.md)
  The size of the image that you want to create.
- [var appearance: NSAppearance?](./appearance.md)
  The visual style (light or dark) to apply to the map when rendering the snapshot image.
- [var scale: CGFloat](./scale.md)
  The scale factor to use when creating the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/traitcollection)*