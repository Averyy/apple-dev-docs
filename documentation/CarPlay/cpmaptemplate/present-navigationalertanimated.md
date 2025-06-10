# present(navigationAlert:animated:)

**Framework**: CarPlay  
**Kind**: method

Displays a navigation alert on the map template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func present(navigationAlert: CPNavigationAlert, animated: Bool)
```

#### Discussion

This method has no effect when the map template is already displaying a navigation alert. Dismiss the current alert before presenting a new one.

## Parameters

- `navigationAlert`: The navigation alert to display.
- `animated`: To animate the display of the alert, set to  ; otherwise, set to   to immediately display the alert.

## See Also

- [func dismissNavigationAlert(animated: Bool, completion: (Bool) -> Void)](cpmaptemplate/dismissnavigationalert(animated:completion:).md)
  Tells the map template to dismiss the visable navigation alert.
- [var currentNavigationAlert: CPNavigationAlert?](cpmaptemplate/currentnavigationalert.md)
  The visible navigation alert.
- [class CPNavigationAlert](cpnavigationalert.md)
  An alert that displays map- or navigation-related information to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/present(navigationalert:animated:))*