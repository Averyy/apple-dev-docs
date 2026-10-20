# image()

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Returns the current contents of the image accumulator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func image() -> CIImage
```

```objc
- (CIImage *) image;
```

#### Return Value

The  image object that represents the current contents of the image accumulator.

## See Also

### Obtaining Data From an Image Accumulator
- [var extent: CGRect](./extent.md)
  The extent of the image associated with the image accumulator.
- [var format: CIFormat](./format.md)
  The pixel format of the image accumulator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/image())*