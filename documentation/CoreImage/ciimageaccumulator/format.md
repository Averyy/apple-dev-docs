# format

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The pixel format of the image accumulator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var format: CIFormat { get }
```

```objc
@property (readonly) CIFormat format;
```

#### Discussion

For applicable values, see Pixel Formats.

## See Also

### Obtaining Data From an Image Accumulator
- [var extent: CGRect](./extent.md)
  The extent of the image associated with the image accumulator.
- [func image() -> CIImage](./image%28%29.md)
  Returns the current contents of the image accumulator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/format)*