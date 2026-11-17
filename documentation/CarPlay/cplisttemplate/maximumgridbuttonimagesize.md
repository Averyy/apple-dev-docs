# maximumGridButtonImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The expected image size for any grid buttons you add to the header.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var maximumGridButtonImageSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumGridButtonImageSize;
```

## Discussion

This property specifies the size of the image in points. The trait collection in your [`CPInterfaceController`](../cpinterfacecontroller.md) provides the scale factor to apply to this size to get the image’s dimensions in pixels.

## See Also

### Getting the configuration limits
- [class var maximumSectionCount: Int](./maximumsectioncount.md)
  The maximum number of sections the template can display.
- [class var maximumItemCount: Int](./maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [class var maximumHeaderGridButtonCount: Int](./maximumheadergridbuttoncount.md)
  The maximum number of grid buttons you can display in the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumgridbuttonimagesize)*