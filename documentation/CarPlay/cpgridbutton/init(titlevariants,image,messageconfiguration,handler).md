# init(titleVariants:image:messageConfiguration:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initialize a button with a title, image, and message configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(titleVariants: [String], image: UIImage, messageConfiguration: CPMessageGridItemConfiguration?, handler: ((CPGridButton) -> Void)? = nil)
```

```objc
- (instancetype) initWithTitleVariants:(NSArray<NSString *> *) titleVariants image:(UIImage *) image messageConfiguration:(CPMessageGridItemConfiguration *) messageConfiguration handler:(void (^)(CPGridButton *gridButton)) handler;
```

## See Also

### Creating a grid button
- [convenience init(titleVariants: [String], image: UIImage, handler: ((CPGridButton) -> Void)?)](./init%28titlevariants,image,handler%29.md)
  Creates a grid button with the specified title variants, image, and action handler.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton/init(titlevariants:image:messageconfiguration:handler:))*