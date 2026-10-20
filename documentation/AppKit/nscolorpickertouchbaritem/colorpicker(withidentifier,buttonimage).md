# colorPicker(withIdentifier:buttonImage:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a color picker bar item using the supplied image as its icon.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

*Mac Catalyst*

```swift
class func colorPicker(withIdentifier identifier: NSTouchBarItem.Identifier, buttonImage image: UIImage) -> Self
```

*macOS*

```swift
class func colorPicker(withIdentifier identifier: NSTouchBarItem.Identifier, buttonImage image: NSImage) -> Self
```

*Mac Catalyst*

```objc
+ (instancetype) colorPickerWithIdentifier:(NSTouchBarItemIdentifier) identifier buttonImage:(UIImage *) image;
```

*macOS*

```objc
+ (instancetype) colorPickerWithIdentifier:(NSTouchBarItemIdentifier) identifier buttonImage:(NSImage *) image;
```

## See Also

### Creating a color picker item
- [class func colorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](./colorpicker%28withidentifier%29.md)
  Creates a bar item with the standard color picker icon.
- [class func textColorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](./textcolorpicker%28withidentifier%29.md)
  Creates a bar item with the standard text color picker icon.
- [class func strokeColorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](./strokecolorpicker%28withidentifier%29.md)
  Creates a bar item with the standard stroke color picker icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/colorpicker(withidentifier:buttonimage:))*