# textField

**Framework**: AppKit  
**Kind**: property

A text field outlet that you can use to display a string.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
@MainActor weak var textField: NSTextField? { get set }
```

#### Discussion

This is a convenience property for accessing a text field in your item’s view hierarchy. Normally, you configure this property in Interface Builder by connecting it to one of your item’s text fields.

## See Also

- [var imageView: NSImageView?](nscollectionviewitem/imageview.md)
  An image view outlet that you can use to display images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/textfield)*