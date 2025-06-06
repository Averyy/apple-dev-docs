# init(rootViewController:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a newly created navigation controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(rootViewController: UIViewController)
```

#### Return Value

The initialized navigation controller object or `nil` if there was a problem initializing the object.

#### Discussion

This is a convenience method for initializing the receiver and pushing a root view controller onto the navigation stack. Every navigation stack must have at least one view controller to act as the root.

## Parameters

- `rootViewController`: The view controller that resides at the bottom of the navigation stack. This object cannot be an instance of the   class.

## See Also

- [init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)](uinavigationcontroller/init(navigationbarclass:toolbarclass:).md)
  Initializes and returns a newly created navigation controller that uses your custom bar subclasses.
- [init(nibName: String?, bundle: Bundle?)](uinavigationcontroller/init(nibname:bundle:).md)
  Creates a navigation controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uinavigationcontroller/init(coder:).md)
  Creates a navigation controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/init(rootviewcontroller:))*