# numberOfColumns

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The number of columns if section content is displayed in a grid layout.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var numberOfColumns: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger numberOfColumns;
```

## Discussion

The number of columns informs the suggested layout of the content, in resolution-independent grid space units. One grid space unit is defined as the width of the project canvas divided by `numberOfColumns`.

## See Also

### Determining Content Properties
- [var elements: [PHProjectElement]](./elements.md)
  An array of asset, text, or journal entry elements contained in the content.
- [var aspectRatio: Double](./aspectratio.md)
  The aspect ratio of the full content layout, defined as width over height.
- [var cloudAssetIdentifiers: [PHCloudIdentifier]](./cloudassetidentifiers.md)
  An array containing all cloud asset identifiers referenced in the content.
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the section content when created from an Apple Print Product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsectioncontent/numberofcolumns)*