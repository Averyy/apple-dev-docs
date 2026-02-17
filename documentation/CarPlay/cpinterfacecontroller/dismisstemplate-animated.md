# dismissTemplate(animated:)

**Framework**: CarPlay  
**Kind**: method

Dismisses the template that the interface controller is displaying modally.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func dismissTemplate(animated: Bool)
```

#### Discussion

Calling this method when there’s no modal template displayed has no effect.

## Parameters

- `animated`: A Boolean value that indicates whether the system animates the dismissal of the template. Set to   to animate the transition.

## See Also

- [func setRootTemplate(CPTemplate, animated: Bool)](cpinterfacecontroller/setroottemplate(_:animated:).md)
  Sets the root template, starting a new stack for the template navigation hierarchy.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/dismisstemplate(animated:))*