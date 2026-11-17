# maximumGridButtonImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The expected image size for your @c CPGridButton.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var maximumGridButtonImageSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumGridButtonImageSize;
```

## Discussion

To properly size your list images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].

## See Also

### Creating a grid template
- [init(title: String?, gridButtons: [CPGridButton])](./init%28title,gridbuttons%29.md)
  Creates a grid template with a title and a set of buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridtemplate/maximumgridbuttonimagesize)*