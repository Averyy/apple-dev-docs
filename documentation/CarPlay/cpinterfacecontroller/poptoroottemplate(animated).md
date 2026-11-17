# popToRootTemplate(animated:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Pop back to the first template in the template navigation hierarchy.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
func popToRootTemplate(animated: Bool)
```

```objc
- (void) popToRootTemplateAnimated:(BOOL) animated;
```

## See Also

### Deprecated
- [func dismissTemplate(animated: Bool)](./dismisstemplate%28animated%29.md)
  Dismiss the current modally-presented template, optionally animating the dismissal.
- [func pop(to: CPTemplate, animated: Bool)](./pop%28to,animated%29.md)
  Pop back to a specified template.
- [func popTemplate(animated: Bool)](./poptemplate%28animated%29.md)
  Pop back a single level in the template navigation hierarchy.
- [func presentTemplate(CPTemplate, animated: Bool)](./presenttemplate%28_,animated%29.md)
  Present a template modally over the navigation hierarchy. Only one template may be presented at a time.
- [func pushTemplate(CPTemplate, animated: Bool)](./pushtemplate%28_,animated%29.md)
  Push a new template onto the template navigation hierarchy, showing it immediately.
- [func setRootTemplate(CPTemplate, animated: Bool)](./setroottemplate%28_,animated%29.md)
  Set the root template. If no existing templates exist in the template navigation hierarchy, the animated flag will be ignored. If there is an existing template navigation hierarchy, the existing stack will be replaced by the new root template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/poptoroottemplate(animated:))*