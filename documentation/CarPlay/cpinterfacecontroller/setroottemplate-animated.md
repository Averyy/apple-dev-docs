# setRootTemplate(_:animated:)

**Framework**: CarPlay  
**Kind**: method

Sets the root template, starting a new stack for the template navigation hierarchy.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool)
```

## Parameters

- `rootTemplate`: The root template. Replaces the current  , if one exists.
- `animated`: Set to   to animate the presentation of the root template; ignored if there isn’t a current  .

## See Also

- [func pushTemplate(CPTemplate, animated: Bool)](cpinterfacecontroller/pushtemplate(_:animated:).md)
  Pushes a template onto the navigation stack and updates the CarPlay display.
- [func popTemplate(animated: Bool)](cpinterfacecontroller/poptemplate(animated:).md)
  Pops the top template from the navigation stack and updates the CarPlay display.
- [func popToRootTemplate(animated: Bool)](cpinterfacecontroller/poptoroottemplate(animated:).md)
  Pops all templates on the stack—except the root template—and updates the CarPlay display.
- [func pop(to: CPTemplate, animated: Bool)](cpinterfacecontroller/pop(to:animated:).md)
  Pops templates until the specified template is at the top of the navigation stack.
- [func presentTemplate(CPTemplate, animated: Bool)](cpinterfacecontroller/presenttemplate(_:animated:).md)
  Presents a template modally.
- [func dismissTemplate(animated: Bool)](cpinterfacecontroller/dismisstemplate(animated:).md)
  Dismisses the template that the interface controller is displaying modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/setroottemplate(_:animated:))*