# dismissNavigationAlert(animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the map template to dismiss the visable navigation alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func dismissNavigationAlert(animated: Bool, completion: @escaping (Bool) -> Void)
```

```swift
func dismissNavigationAlert(animated: Bool) async -> Bool
```

```objc
- (void) dismissNavigationAlertAnimated:(BOOL) animated completion:(void (^)(BOOL dismissed)) completion;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func dismissNavigationAlert(animated: Bool) async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `animated`: Determines whether the system should animate the dismissal of the navigation alert. Set to [`true`](../../Swift/true.md) to animate the dismissal.
- `completion`: The block invoked after dismissing the navigation alert. The [`Bool`](../../Swift/bool.md) argument in the block indicates whether the template dismissed an alert.

## See Also

### Displaying a Navigation Alert
- [func present(navigationAlert: CPNavigationAlert, animated: Bool)](./present%28navigationalert,animated%29.md)
  Displays a navigation alert on the map template.
- [var currentNavigationAlert: CPNavigationAlert?](./currentnavigationalert.md)
  The visible navigation alert.
- [class CPNavigationAlert](../cpnavigationalert.md)
  An alert that displays map- or navigation-related information to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/dismissnavigationalert(animated:completion:))*