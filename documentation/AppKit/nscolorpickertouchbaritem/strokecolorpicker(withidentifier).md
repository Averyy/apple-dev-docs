# strokeColorPicker(withIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a bar item with the standard stroke color picker icon.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
class func strokeColorPicker(withIdentifier identifier: NSTouchBarItem.Identifier) -> Self
```

```objc
+ (instancetype) strokeColorPickerWithIdentifier:(NSTouchBarItemIdentifier) identifier;
```

## See Also

### Creating a color picker item
- [class func colorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](./colorpicker%28withidentifier%29.md)
  Creates a bar item with the standard color picker icon.
- [class func textColorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](./textcolorpicker%28withidentifier%29.md)
  Creates a bar item with the standard text color picker icon.
- [class func colorPicker(withIdentifier: NSTouchBarItem.Identifier, buttonImage: UIImage) -> Self](./colorpicker%28withidentifier,buttonimage%29.md)
  Creates a color picker bar item using the supplied image as its icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/strokecolorpicker(withidentifier:))*