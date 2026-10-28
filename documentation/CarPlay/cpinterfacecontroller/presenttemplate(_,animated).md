# presentTemplate(_:animated:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Presents a template modally.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

> **Deprecated**: Use [`presentTemplate(_:animated:completion:)`](./presenttemplate%28_,animated,completion%29.md) instead.

## Declaration

```swift
func presentTemplate(_ templateToPresent: CPTemplate, animated: Bool)
```

```objc
- (void) presentTemplate:(CPTemplate *) templateToPresent animated:(BOOL) animated;
```

## Discussion

You can present only one template at a time.

## Parameters

- `templateToPresent`: A template to display over currently displayed content on the CarPlay screen. The template must be one of the following types:

  - [`CPActionSheetTemplate`](../cpactionsheettemplate.md)
  - [`CPAlertTemplate`](../cpalerttemplate.md)
  - [`CPVoiceControlTemplate`](../cpvoicecontroltemplate.md)
- `animated`: A Boolean value that indicates whether the system animates the display of transitioning templates. Set to [`true`](../../Swift/true.md) to animate the transition.

## See Also

### Deprecated Methods
- [func setRootTemplate(CPTemplate, animated: Bool)](./setroottemplate%28_,animated%29.md)
  Sets the root template, starting a new stack for the template navigation hierarchy.
- [func pushTemplate(CPTemplate, animated: Bool)](./pushtemplate%28_,animated%29.md)
  Pushes a template onto the navigation stack and updates the CarPlay display.
- [func popTemplate(animated: Bool)](./poptemplate%28animated%29.md)
  Pops the top template from the navigation stack and updates the CarPlay display.
- [func popToRootTemplate(animated: Bool)](./poptoroottemplate%28animated%29.md)
  Pops all templates on the stack—except the root template—and updates the CarPlay display.
- [func pop(to: CPTemplate, animated: Bool)](./pop%28to,animated%29.md)
  Pops templates until the specified template is at the top of the navigation stack.
- [func dismissTemplate(animated: Bool)](./dismisstemplate%28animated%29.md)
  Dismisses the template that the interface controller is displaying modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/presenttemplate(_:animated:))*