# sender

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object responsible for the action handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sender: Any? { get }
```

```objc
@property (nonatomic, readonly, nullable) id sender;
```

## See Also

### Getting information about the action
- [var title: String](./title.md)
  The action’s title.
- [var image: UIImage?](./image.md)
  The action’s image.
- [var identifier: UIAction.Identifier](./identifier-swift.property.md)
  The unique identifier for the action.
- [var discoverabilityTitle: String?](./discoverabilitytitle.md)
  An elaborated title that explains the purpose of the action.
- [var attributes: UIMenuElement.Attributes](./attributes.md)
  The attributes indicating the style of the action.
- [var state: UIMenuElement.State](./state.md)
  The state of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/sender)*