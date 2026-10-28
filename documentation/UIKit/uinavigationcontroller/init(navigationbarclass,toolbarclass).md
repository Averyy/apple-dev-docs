# init(navigationBarClass:toolbarClass:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly created navigation controller that uses your custom bar subclasses.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)
```

```objc
- (instancetype) initWithNavigationBarClass:(Class) navigationBarClass toolbarClass:(Class) toolbarClass;
```

## Return Value

The initialized navigation controller object or `nil` if there was a problem initializing the object.

## Discussion

To customize the overall appearance of a navigation bar, use [`UIAppearance`](../uiappearance.md) APIs instead of this method. If you use this initialization method to create a navigation bar that uses custom bar subclasses, you are responsible for pushing and setting view controllers before presenting the navigation controller onscreen.

## Parameters

- `navigationBarClass`: Specify the custom [`UINavigationBar`](../uinavigationbar.md) subclass you want to use, or specify `nil` to use the standard [`UINavigationBar`](../uinavigationbar.md) class.
- `toolbarClass`: Specify the custom [`UIToolbar`](../uitoolbar.md) subclass you want to use, or specify `nil` to use the standard [`UIToolbar`](../uitoolbar.md) class.

## See Also

### Creating a navigation controller
- [init(rootViewController: UIViewController)](./init%28rootviewcontroller%29.md)
  Initializes and returns a newly created navigation controller.
- [init(nibName: String?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Creates a navigation controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a navigation controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/init(navigationbarclass:toolbarclass:))*