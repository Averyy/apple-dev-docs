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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton/init(titlevariants:image:messageconfiguration:handler:))*