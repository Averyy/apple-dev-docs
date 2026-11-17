# maximumHeaderGridButtonCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of grid buttons you can display in the header.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var maximumHeaderGridButtonCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSUInteger maximumHeaderGridButtonCount;
```

## Discussion

If you initialize your list template with more buttons than the maximum, the list template ignores any buttons in your array past the specified maximum.

## See Also

### Getting the configuration limits
- [class var maximumSectionCount: Int](./maximumsectioncount.md)
  The maximum number of sections the template can display.
- [class var maximumItemCount: Int](./maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [class var maximumGridButtonImageSize: CGSize](./maximumgridbuttonimagesize.md)
  The expected image size for any grid buttons you add to the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumheadergridbuttoncount)*