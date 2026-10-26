# cloudAssetIdentifiers

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array containing all cloud asset identifiers referenced in the content.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var cloudAssetIdentifiers: [PHCloudIdentifier] { get }
```

```objc
@property (nonatomic, readonly) NSArray<PHCloudIdentifier *> * cloudAssetIdentifiers;
```

## See Also

### Determining Content Properties
- [var elements: [PHProjectElement]](./elements.md)
  An array of asset, text, or journal entry elements contained in the content.
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns if section content is displayed in a grid layout.
- [var aspectRatio: Double](./aspectratio.md)
  The aspect ratio of the full content layout, defined as width over height.
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the section content when created from an Apple Print Product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsectioncontent/cloudassetidentifiers)*