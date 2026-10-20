# presentedTemplate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The interface controller’s current modal template.

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

## See Also

### Displaying Templates Modally
- [func presentTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./presenttemplate%28_,animated,completion%29.md)
  Presents a template modally.
- [func dismissTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./dismisstemplate%28animated,completion%29.md)
  Dismisses a modal template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/presentedtemplate)*