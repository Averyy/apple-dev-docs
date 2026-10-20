# provideNewButtonImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The button image used by the color picker.

**Availability**:
- macOS

## Declaration

```swift
var provideNewButtonImage: NSImage { get }
```

```objc
@property (strong, readonly) NSImage * provideNewButtonImage;
```

#### Discussion

The image placed on the mode button the user uses to select this color picker. This is the same image the color panel uses as an argument when sending the [`insertNewButtonImage(_:in:)`](./insertnewbuttonimage%28_,in%29.md) message. Override this property’s getter method to provide a custom button image. The default implementation looks in the color picker’s bundle for a TIFF file named after the color picker’s class, with the extension “`.tiff`”.

## See Also

### Adding Button Images
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](./insertnewbuttonimage%28_,in%29.md)
  Sets the image used for the specified button cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker/providenewbuttonimage)*