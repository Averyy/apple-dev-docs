# init(contentViewController:)

**Framework**: UIKit  
**Kind**: init

Returns an initialized popover controller object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
init(contentViewController viewController: UIViewController)
```

#### Return Value

An initialized popover controller object.

#### Discussion

When initializing a popover controller, you must specify the view controller object whose content is to be displayed in the popover. You can change this view controller later by modifying the [`contentViewController`](uipopovercontroller/contentviewcontroller.md) property.

## Parameters

- `viewController`: The view controller for managing the popover’s content. This parameter must not be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/init(contentviewcontroller:))*