# init(presentedViewController:presenting:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a presentation controller for transitioning between the specified view controllers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(presentedViewController: UIViewController, presenting presentingViewController: UIViewController?)
```

```objc
- (instancetype) initWithPresentedViewController:(UIViewController *) presentedViewController presentingViewController:(UIViewController *) presentingViewController;
```

#### Return Value

An initialized presentation controller object or `nil` if the presentation controller could not be initialized.

#### Discussion

This method is the designated initializer for the presentation controller. You must call it from any custom initialization methods you define for your presentation controller subclasses.

## Parameters

- `presentedViewController`: The view controller being presented modally.
- `presentingViewController`: The view controller whose content represents the starting point of the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/init(presentedviewcontroller:presenting:))*