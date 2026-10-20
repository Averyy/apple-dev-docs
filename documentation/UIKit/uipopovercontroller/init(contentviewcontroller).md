# init(contentViewController:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized popover controller object.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
init(contentViewController viewController: UIViewController)
```

```objc
- (instancetype) initWithContentViewController:(UIViewController *) viewController;
```

#### Return Value

An initialized popover controller object.

#### Discussion

When initializing a popover controller, you must specify the view controller object whose content is to be displayed in the popover. You can change this view controller later by modifying the [`contentViewController`](./contentviewcontroller.md) property.

## Parameters

- `viewController`: The view controller for managing the popover’s content. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/init(contentviewcontroller:))*