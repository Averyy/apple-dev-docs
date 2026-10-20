# backgroundColor

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the color used in the background of the thumbnail view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
@NSCopying
var backgroundColor: UIColor? { get set }
```

*macOS*

```swift
@NSCopying
var backgroundColor: NSColor? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) UIColor * backgroundColor;
```

*macOS*

```objc
@property (nonatomic, copy, nullable) NSColor * backgroundColor;
```

#### Return Value

The color of the background in the thumbnail view.

## See Also

### Working with Thumbnail View Display Characteristics
- [var maximumNumberOfColumns: Int](./maximumnumberofcolumns.md)
  Returns the maximum number of columns of thumbnails the thumbnail view can display.
- [var labelFont: NSFont?](./labelfont.md)
  Returns the font used to label the thumbnails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview/backgroundcolor)*