# backgroundColor

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The background color of the section content when created from an Apple Print Product.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var backgroundColor: NSColor? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSColor * backgroundColor;
```

## Discussion

This property has no meaning outside of Apple Print Products.

## See Also

### Determining Content Properties
- [var elements: [PHProjectElement]](./elements.md)
  An array of asset, text, or journal entry elements contained in the content.
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns if section content is displayed in a grid layout.
- [var aspectRatio: Double](./aspectratio.md)
  The aspect ratio of the full content layout, defined as width over height.
- [var cloudAssetIdentifiers: [PHCloudIdentifier]](./cloudassetidentifiers.md)
  An array containing all cloud asset identifiers referenced in the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsectioncontent/backgroundcolor)*