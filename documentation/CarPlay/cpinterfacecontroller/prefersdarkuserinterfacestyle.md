# prefersDarkUserInterfaceStyle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you prefer Dark Mode for your interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var prefersDarkUserInterfaceStyle: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL prefersDarkUserInterfaceStyle;
```

## Discussion

Before you push any templates or install a root template, set this property to `true` to display your app’s content with a dark user interface style. The default value of this property is `false`, which allows content to change between light and dark styles.

## See Also

### Configuring interface-related details
- [var carTraitCollection: UITraitCollection](./cartraitcollection.md)
  The trait collection of the vehicle’s primary screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/prefersdarkuserinterfacestyle)*