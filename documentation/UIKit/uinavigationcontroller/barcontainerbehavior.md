# barContainerBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Whether this navigation controller acts as a bar container, reading the bar content of its child view controller and rendering that content in the navigation controller’s own bar.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var barContainerBehavior: UIBarContainerBehavior { get set }
```

```objc
@property (nonatomic) UIBarContainerBehavior barContainerBehavior;
```

## Discussion

For example, if there is a split view controller where one of the columns is a view controller with multiple child `UINavigationController`s, set `barContainerBehavior` to `.local` on all the children so that each one renders its own toolbar, instead of their toolbar content being rendered in a single toolbar managed by the split view controller.

Defaults to `UIBarContainerBehaviorAutomatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/barcontainerbehavior)*