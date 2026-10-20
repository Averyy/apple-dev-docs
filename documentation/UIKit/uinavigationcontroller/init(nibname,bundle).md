# init(nibName:bundle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a navigation controller with the nib file in the specified bundle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

```objc
- (instancetype) initWithNibName:(NSString *) nibNameOrNil bundle:(NSBundle *) nibBundleOrNil;
```

## See Also

### Creating a navigation controller
- [init(rootViewController: UIViewController)](./init%28rootviewcontroller%29.md)
  Initializes and returns a newly created navigation controller.
- [init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)](./init%28navigationbarclass,toolbarclass%29.md)
  Initializes and returns a newly created navigation controller that uses your custom bar subclasses.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a navigation controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/init(nibname:bundle:))*