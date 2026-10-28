# setImage(_:dirtyRect:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Updates an image accumulator with a subregion of an image object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setImage(_ image: CIImage, dirtyRect: CGRect)
```

```objc
- (void) setImage:(CIImage *) image dirtyRect:(CGRect) dirtyRect;
```

## Discussion

For additional details on using this method, see “Imaging Dynamical Systems” in [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Parameters

- `image`: The image object whose contents you want to assign to the image accumulator.
- `dirtyRect`: A rectangle that defines the subregion of the image object that’s changed since the last time you updated the image accumulator. You must guarantee that the new contents differ from the old only within the region specified by the this argument.

## See Also

### Setting an Image
- [func setImage(CIImage)](./setimage%28_%29.md)
  Sets the contents of the image accumulator to the contents of the specified image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/setimage(_:dirtyrect:))*