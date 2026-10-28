# currentNavigationAlert

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The visible navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var currentNavigationAlert: CPNavigationAlert? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) CPNavigationAlert * currentNavigationAlert;
```

## Discussion

If a navigation alert isn’t visible, the property returns [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Displaying a Navigation Alert
- [func present(navigationAlert: CPNavigationAlert, animated: Bool)](./present%28navigationalert,animated%29.md)
  Displays a navigation alert on the map template.
- [func dismissNavigationAlert(animated: Bool, completion: (Bool) -> Void)](./dismissnavigationalert%28animated,completion%29.md)
  Tells the map template to dismiss the visable navigation alert.
- [class CPNavigationAlert](../cpnavigationalert.md)
  An alert that displays map- or navigation-related information to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/currentnavigationalert)*