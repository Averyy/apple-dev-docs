# isValid

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether it is possible to draw an image representation.

**Availability**:
- macOS

## Declaration

```swift
var isValid: Bool { get }
```

```objc
@property (readonly, getter=isValid) BOOL valid;
```

## Discussion

If you created the image with an existing image file, but the corresponding image data is not yet loaded into memory, this method loads the data and expands it as needed. If the receiver contains no image representations and no associated image file, this method creates a valid cached image representation and initializes it to the default bit depth. If the file or URL from which the image was initialized is nonexistent, or the data in an existing file is invalid, this method returns [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [convenience init?(byReferencingFile: String)](./init%28byreferencingfile%29.md)
  Initializes and returns an image object using the specified file.
- [convenience init(byReferencing: URL)](./init%28byreferencing%29.md)
  Initializes and returns an image object using the specified URL.
### Managing Drawing Options
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color for the image.
- [var capInsets: NSEdgeInsets](./capinsets.md)
  The cap insets for the image.
- [var resizingMode: NSImage.ResizingMode](./resizingmode-swift.property.md)
  The resizing mode for the image.
- [NSImage.ResizingMode](./resizingmode-swift.enum.md)
  Constants that describe the resizing mode for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/isvalid)*