# imageView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An image view outlet that you can use to display images.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
weak var imageView: NSImageView? { get set }
```

```objc
@property (weak, nullable) NSImageView * imageView;
```

#### Discussion

This is a convenience property for accessing an image view in your item’s view hierarchy. Normally, you configure this property in Interface Builder by connecting it to one of your item’s image views.

## See Also

### Getting and Setting Image and Text Fields
- [var textField: NSTextField?](./textfield.md)
  A text field outlet that you can use to display a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/imageview)*