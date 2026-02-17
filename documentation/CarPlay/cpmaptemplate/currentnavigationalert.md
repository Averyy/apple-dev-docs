# currentNavigationAlert

**Framework**: CarPlay  
**Kind**: property

The visible navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var currentNavigationAlert: CPNavigationAlert? { get }
```

#### Discussion

If a navigation alert isn’t visible, the property returns [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0).

## See Also

- [func present(navigationAlert: CPNavigationAlert, animated: Bool)](cpmaptemplate/present(navigationalert:animated:).md)
  Displays a navigation alert on the map template.
- [func dismissNavigationAlert(animated: Bool, completion: (Bool) -> Void)](cpmaptemplate/dismissnavigationalert(animated:completion:).md)
  Tells the map template to dismiss the visable navigation alert.
- [class CPNavigationAlert](cpnavigationalert.md)
  An alert that displays map- or navigation-related information to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/currentnavigationalert)*