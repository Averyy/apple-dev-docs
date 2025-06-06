# templateWillDisappear(_:animated:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the template will disappear from the screen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func templateWillDisappear(_ aTemplate: CPTemplate, animated: Bool)
```

## Parameters

- `animated`: A Boolean value indicating whether the system animates the disappearance of the template.

## See Also

- [func templateWillAppear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatewillappear(_:animated:).md)
  Tells the delegate that the template will appear onscreen.
- [func templateDidAppear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatedidappear(_:animated:).md)
  Tells the delegate that the template did appear onscreen.
- [func templateDidDisappear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatediddisappear(_:animated:).md)
  Tells the delegate that the template did disappear from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontrollerdelegate/templatewilldisappear(_:animated:))*