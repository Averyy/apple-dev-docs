# templateDidDisappear(_:animated:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the template did disappear from the screen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func templateDidDisappear(_ aTemplate: CPTemplate, animated: Bool)
```

## Parameters

- `animated`: A Boolean value indicating whether the system animated the disappearance of the template.

## See Also

- [func templateWillAppear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatewillappear(_:animated:).md)
  Tells the delegate that the template will appear onscreen.
- [func templateDidAppear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatedidappear(_:animated:).md)
  Tells the delegate that the template did appear onscreen.
- [func templateWillDisappear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatewilldisappear(_:animated:).md)
  Tells the delegate that the template will disappear from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontrollerdelegate/templatediddisappear(_:animated:))*