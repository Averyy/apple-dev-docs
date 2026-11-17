# presentedTemplate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The current modally-presented template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var presentedTemplate: CPTemplate? { get }
```

```objc
@property (nonatomic, readonly, nullable) CPTemplate * presentedTemplate;
```

## Discussion

To present a template modally from your app’s interface, call the [`presentTemplate(_:animated:completion:)`](./presenttemplate%28_,animated,completion%29.md) method. If there isn’t a modally presented template currently, the value of this property is `nil`.

## See Also

### Presenting a template modally
- [func presentTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./presenttemplate%28_,animated,completion%29.md)
  Presents the template modally over your app’s navigation interface.
- [func dismissTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./dismisstemplate%28animated,completion%29.md)
  Dismisses the template you previously presented modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/presentedtemplate)*