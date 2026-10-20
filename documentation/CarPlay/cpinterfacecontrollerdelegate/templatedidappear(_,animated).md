# templateDidAppear(_:animated:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the template did appear onscreen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateDidAppear(_ aTemplate: CPTemplate, animated: Bool)
```

```objc
- (void) templateDidAppear:(CPTemplate *) aTemplate animated:(BOOL) animated;
```

## Parameters

- `animated`: A Boolean value indicating whether the system animated the presentation of the template.

## See Also

### Handling Display Events
- [func templateWillAppear(CPTemplate, animated: Bool)](./templatewillappear%28_,animated%29.md)
  Tells the delegate that the template will appear onscreen.
- [func templateWillDisappear(CPTemplate, animated: Bool)](./templatewilldisappear%28_,animated%29.md)
  Tells the delegate that the template will disappear from the screen.
- [func templateDidDisappear(CPTemplate, animated: Bool)](./templatediddisappear%28_,animated%29.md)
  Tells the delegate that the template did disappear from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontrollerdelegate/templatedidappear(_:animated:))*