# rootTemplate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The root template in the navigation hierarchy.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var rootTemplate: CPTemplate { get }
```

```objc
@property (nonatomic, readonly) CPTemplate * rootTemplate;
```

## Discussion

The root template represents your app’s initial interface, and is the starting point from which someone explores your app’s content. Use this property to get the root template. To install or change the root template, call the [`setRootTemplate(_:animated:completion:)`](./setroottemplate%28_,animated,completion%29.md) method.

## See Also

### Getting the current templates
- [var topTemplate: CPTemplate?](./toptemplate.md)
  The top-most template in your app’s navigation hierarchy.
- [var templates: [CPTemplate]](./templates.md)
  The templates currently in your app’s navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/roottemplate)*