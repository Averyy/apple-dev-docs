# elements

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array of asset, text, or journal entry elements contained in the content.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var elements: [PHProjectElement] { get }
```

```objc
@property (nonatomic, readonly) NSArray<__kindof PHProjectElement *> * elements;
```

## See Also

### Determining Content Properties
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns if section content is displayed in a grid layout.
- [var aspectRatio: Double](./aspectratio.md)
  The aspect ratio of the full content layout, defined as width over height.
- [var cloudAssetIdentifiers: [PHCloudIdentifier]](./cloudassetidentifiers.md)
  An array containing all cloud asset identifiers referenced in the content.
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The background color of the section content when created from an Apple Print Product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsectioncontent/elements)*