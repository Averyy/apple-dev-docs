# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a navigation controller from data in an unarchiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## See Also

### Creating a navigation controller
- [init(rootViewController: UIViewController)](./init%28rootviewcontroller%29.md)
  Initializes and returns a newly created navigation controller.
- [init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)](./init%28navigationbarclass,toolbarclass%29.md)
  Initializes and returns a newly created navigation controller that uses your custom bar subclasses.
- [init(nibName: String?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Creates a navigation controller with the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/init(coder:))*