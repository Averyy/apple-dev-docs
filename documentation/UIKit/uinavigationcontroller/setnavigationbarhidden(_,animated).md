# setNavigationBarHidden(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the navigation bar is hidden.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setNavigationBarHidden(_ hidden: Bool, animated: Bool)
```

```objc
- (void) setNavigationBarHidden:(BOOL) hidden animated:(BOOL) animated;
```

#### Discussion

For animated transitions, the duration of the animation is specified by the value in the [`hideShowBarDuration`](./hideshowbarduration.md) constant.

## Parameters

- `hidden`: Specify [`true`](../../Swift/true.md) to hide the navigation bar or [`false`](../../Swift/false.md) to show it.
- `animated`: Specify [`true`](../../Swift/true.md) if you want to animate the change in visibility or [`false`](../../Swift/false.md) if you want the navigation bar to appear immediately.

## See Also

### Related Documentation
- [var isNavigationBarHidden: Bool](./isnavigationbarhidden.md)
  A Boolean value that indicates whether the navigation bar is hidden.
### Configuring navigation bars
- [var navigationBar: UINavigationBar](./navigationbar.md)
  The navigation bar managed by the navigation controller.
- [Customizing your app’s navigation bar](../customizing-your-app-s-navigation-bar.md)
  Create custom titles, prompts, and buttons in your app’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/setnavigationbarhidden(_:animated:))*