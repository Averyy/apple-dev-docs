# setRootTemplate(_:animated:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Sets the root template, starting a new stack for the template navigation hierarchy.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

> **Deprecated**: Use [`setRootTemplate(_:animated:completion:)`](./setroottemplate%28_,animated,completion%29.md) instead.

## Declaration

```swift
func setRootTemplate(_ rootTemplate: CPTemplate, animated: Bool)
```

```objc
- (void) setRootTemplate:(CPTemplate *) rootTemplate animated:(BOOL) animated;
```

## Parameters

- `rootTemplate`: The root template. Replaces the current [`rootTemplate`](./roottemplate.md), if one exists.
- `animated`: Set to [`true`](../../Swift/true.md) to animate the presentation of the root template; ignored if there isn’t a current [`rootTemplate`](./roottemplate.md).

## See Also

### Deprecated Methods
- [func pushTemplate(CPTemplate, animated: Bool)](./pushtemplate%28_,animated%29.md)
  Pushes a template onto the navigation stack and updates the CarPlay display.
- [func popTemplate(animated: Bool)](./poptemplate%28animated%29.md)
  Pops the top template from the navigation stack and updates the CarPlay display.
- [func popToRootTemplate(animated: Bool)](./poptoroottemplate%28animated%29.md)
  Pops all templates on the stack—except the root template—and updates the CarPlay display.
- [func pop(to: CPTemplate, animated: Bool)](./pop%28to,animated%29.md)
  Pops templates until the specified template is at the top of the navigation stack.
- [func presentTemplate(CPTemplate, animated: Bool)](./presenttemplate%28_,animated%29.md)
  Presents a template modally.
- [func dismissTemplate(animated: Bool)](./dismisstemplate%28animated%29.md)
  Dismisses the template that the interface controller is displaying modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/setroottemplate(_:animated:))*