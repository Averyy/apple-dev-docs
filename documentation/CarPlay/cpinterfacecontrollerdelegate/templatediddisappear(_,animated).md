# templateDidDisappear(_:animated:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the controller removed the specified template from your interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateDidDisappear(_ aTemplate: CPTemplate, animated: Bool)
```

```objc
- (void) templateDidDisappear:(CPTemplate *) aTemplate animated:(BOOL) animated;
```

## Discussion

The interface controller calls this method shortly after removing `aTemplate` from your app’s interface. If `animated` is `true`, this method runs after the animations finish. Use this method to perform additional tasks after the template disappears

## Parameters

- `aTemplate`: The template that disappeared.
- `animated`: `true` if the system animated the disappearance of the template.

## See Also

### Handling display-related events
- [func templateWillAppear(CPTemplate, animated: Bool)](./templatewillappear%28_,animated%29.md)
  Tells the delegate that the controller is about to show the specified template in your interface.
- [func templateDidAppear(CPTemplate, animated: Bool)](./templatedidappear%28_,animated%29.md)
  Tells the delegate that the controller showed the specified template in your interface.
- [func templateWillDisappear(CPTemplate, animated: Bool)](./templatewilldisappear%28_,animated%29.md)
  Tells the delegate that the controller is about to remove the specified template in your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontrollerdelegate/templatediddisappear(_:animated:))*