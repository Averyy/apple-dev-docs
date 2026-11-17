# topTemplate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The top-most template in your app’s navigation hierarchy.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var topTemplate: CPTemplate? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) CPTemplate * topTemplate;
```

## Discussion

This property stores the top-most template in your app’s navigation stack. The navigation stack includes the root template and the templates you pushed onto the stack using the [`pushTemplate(_:animated:completion:)`](./pushtemplate%28_,animated,completion%29.md) method. It doesn’t include templates you removed from the stack or templates you presented modally or using an overlay. If you haven’t yet installed a root template, this property is `nil`.

## See Also

### Getting the current templates
- [var rootTemplate: CPTemplate](./roottemplate.md)
  The root template in the navigation hierarchy.
- [var templates: [CPTemplate]](./templates.md)
  The templates currently in your app’s navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/toptemplate)*