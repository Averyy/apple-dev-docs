# showsDisclosureIndicator

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the list item cell shows a disclosure indicator on its trailing edge.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0 (renamed: CPListItemAccessoryType)
- iPadOS 12.0+ - Deprecated in 14.0 (renamed: CPListItemAccessoryType)
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: CPListItemAccessoryType)

> **Deprecated**: Use [`accessoryType`](./accessorytype.md) instead.

## Declaration

```swift
var showsDisclosureIndicator: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL showsDisclosureIndicator;
```

## See Also

### Deprecated Properties
- [var showsExplicitLabel: Bool](./showsexplicitlabel.md)
  A Boolean value that determines whether the list item displays its explicit content indicator.
- [func setRootTemplate(CPTemplate, animated: Bool)](../cpinterfacecontroller/setroottemplate%28_,animated%29.md)
  Sets the root template, starting a new stack for the template navigation hierarchy.
- [func pushTemplate(CPTemplate, animated: Bool)](../cpinterfacecontroller/pushtemplate%28_,animated%29.md)
  Pushes a template onto the navigation stack and updates the CarPlay display.
- [func popTemplate(animated: Bool)](../cpinterfacecontroller/poptemplate%28animated%29.md)
  Pops the top template from the navigation stack and updates the CarPlay display.
- [func popToRootTemplate(animated: Bool)](../cpinterfacecontroller/poptoroottemplate%28animated%29.md)
  Pops all templates on the stack—except the root template—and updates the CarPlay display.
- [func pop(to: CPTemplate, animated: Bool)](../cpinterfacecontroller/pop%28to,animated%29.md)
  Pops templates until the specified template is at the top of the navigation stack.
- [func presentTemplate(CPTemplate, animated: Bool)](../cpinterfacecontroller/presenttemplate%28_,animated%29.md)
  Presents a template modally.
- [func dismissTemplate(animated: Bool)](../cpinterfacecontroller/dismisstemplate%28animated%29.md)
  Dismisses the template that the interface controller is displaying modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/showsdisclosureindicator)*