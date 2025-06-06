# init(navigationBarClass:toolbarClass:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a newly created navigation controller that uses your custom bar subclasses.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)
```

#### Return Value

The initialized navigation controller object or `nil` if there was a problem initializing the object.

#### Discussion

To customize the overall appearance of a navigation bar, use [`UIAppearance`](uiappearance.md) APIs instead of this method. If you use this initialization method to create a navigation bar that uses custom bar subclasses, you are responsible for pushing and setting view controllers before presenting the navigation controller onscreen.

## Parameters

- `navigationBarClass`: Specify the custom   subclass you want to use, or specify   to use the standard   class.
- `toolbarClass`: Specify the custom   subclass you want to use, or specify   to use the standard   class.

## See Also

- [init(rootViewController: UIViewController)](uinavigationcontroller/init(rootviewcontroller:).md)
  Initializes and returns a newly created navigation controller.
- [init(nibName: String?, bundle: Bundle?)](uinavigationcontroller/init(nibname:bundle:).md)
  Creates a navigation controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uinavigationcontroller/init(coder:).md)
  Creates a navigation controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/init(navigationbarclass:toolbarclass:))*