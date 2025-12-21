# isValid

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether it is possible to draw an image representation.

**Availability**:
- macOS ?+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

If you created the image with an existing image file, but the corresponding image data is not yet loaded into memory, this method loads the data and expands it as needed. If the receiver contains no image representations and no associated image file, this method creates a valid cached image representation and initializes it to the default bit depth. If the file or URL from which the image was initialized is nonexistent, or the data in an existing file is invalid, this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [convenience init?(byReferencingFile: String)](nsimage/init(byreferencingfile:).md)
  Initializes and returns an image object using the specified file.
- [convenience init(byReferencing: URL)](nsimage/init(byreferencing:).md)
  Initializes and returns an image object using the specified URL.
- [var backgroundColor: NSColor](nsimage/backgroundcolor.md)
  The background color for the image.
- [var capInsets: NSEdgeInsets](nsimage/capinsets.md)
  The cap insets for the image.
- [var resizingMode: NSImage.ResizingMode](nsimage/resizingmode-swift.property.md)
  The resizing mode for the image.
- [NSImage.ResizingMode](nsimage/resizingmode-swift.enum.md)
  Constants that describe the resizing mode for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/isvalid)*