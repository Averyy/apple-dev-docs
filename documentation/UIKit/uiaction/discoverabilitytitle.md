# discoverabilityTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An elaborated title that explains the purpose of the action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var discoverabilityTitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * discoverabilityTitle;
```

## Discussion

The system uses this property to display information about the command. In iOS, the system displays this title in the discoverability heads-up display (HUD). If this property is `nil`, the HUD displays the [`title`](./title.md) property.

In Mac apps built with Mac Catalyst, the system displays the discoverability title as a tooltip.

## See Also

### Getting information about the action
- [var title: String](./title.md)
  The action’s title.
- [var image: UIImage?](./image.md)
  The action’s image.
- [var identifier: UIAction.Identifier](./identifier-swift.property.md)
  The unique identifier for the action.
- [var attributes: UIMenuElement.Attributes](./attributes.md)
  The attributes indicating the style of the action.
- [var state: UIMenuElement.State](./state.md)
  The state of the action.
- [var sender: Any?](./sender.md)
  The object responsible for the action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/discoverabilitytitle)*