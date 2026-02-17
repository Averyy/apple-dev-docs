# showsExplicitLabel

**Framework**: CarPlay  
**Kind**: property

A Boolean value that determines whether the list item displays its explicit content indicator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var showsExplicitLabel: Bool { get set }
```

## See Also

- [var showsDisclosureIndicator: Bool](cplistitem/showsdisclosureindicator.md)
  A Boolean value that indicates whether the list item cell shows a disclosure indicator on its trailing edge.
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
- [func dismissTemplate(animated: Bool)](cpinterfacecontroller/dismisstemplate(animated:).md)
  Dismisses the template that the interface controller is displaying modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/showsexplicitlabel)*