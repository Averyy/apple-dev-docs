# textField

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A text field outlet that you can use to display a string.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
weak var textField: NSTextField? { get set }
```

```objc
@property (weak, nullable) NSTextField * textField;
```

#### Discussion

This is a convenience property for accessing a text field in your item’s view hierarchy. Normally, you configure this property in Interface Builder by connecting it to one of your item’s text fields.

## See Also

### Getting and Setting Image and Text Fields
- [var imageView: NSImageView?](./imageview.md)
  An image view outlet that you can use to display images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/textfield)*