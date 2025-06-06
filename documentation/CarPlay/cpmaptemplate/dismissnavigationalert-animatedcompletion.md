# dismissNavigationAlert(animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Tells the map template to dismiss the visable navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func dismissNavigationAlert(animated: Bool) async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func dismissNavigationAlert(animated: Bool) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func dismissNavigationAlert(animated: Bool) async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `animated`: Determines whether the system should animate the dismissal of the navigation alert. Set to   to animate the dismissal.
- `completion`: The block invoked after dismissing the navigation alert. The   argument in the block indicates whether the template dismissed an alert.

## See Also

- [func present(navigationAlert: CPNavigationAlert, animated: Bool)](cpmaptemplate/present(navigationalert:animated:).md)
  Displays a navigation alert on the map template.
- [var currentNavigationAlert: CPNavigationAlert?](cpmaptemplate/currentnavigationalert.md)
  The visible navigation alert.
- [class CPNavigationAlert](cpnavigationalert.md)
  An alert that displays map- or navigation-related information to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/dismissnavigationalert(animated:completion:))*