# setImage(_:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Sets the contents of the image accumulator to the contents of the specified image object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setImage(_ image: CIImage)
```

```objc
- (void) setImage:(CIImage *) image;
```

## Parameters

- `image`: The image object whose contents you want to assign to the image accumulator.

## See Also

### Setting an Image
- [func setImage(CIImage, dirtyRect: CGRect)](./setimage%28_,dirtyrect%29.md)
  Updates an image accumulator with a subregion of an image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/setimage(_:))*