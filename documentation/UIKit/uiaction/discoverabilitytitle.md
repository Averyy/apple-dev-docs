# discoverabilityTitle

**Framework**: UIKit  
**Kind**: property

An elaborated title that explains the purpose of the action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var discoverabilityTitle: String? { get set }
```

#### Discussion

The system uses this property to display information about the command. In iOS, the system displays this title in the discoverability heads-up display (HUD). If this property is `nil`, the HUD displays the [`title`](uiaction/title.md) property.

In Mac apps built with Mac Catalyst, the system displays the discoverability title as a tooltip.

## See Also

- [var title: String](uiaction/title.md)
  The action’s title.
- [var image: UIImage?](uiaction/image.md)
  The action’s image.
- [var identifier: UIAction.Identifier](uiaction/identifier-swift.property.md)
  The unique identifier for the action.
- [var attributes: UIMenuElement.Attributes](uiaction/attributes.md)
  The attributes indicating the style of the action.
- [var state: UIMenuElement.State](uiaction/state.md)
  The state of the action.
- [var sender: Any?](uiaction/sender.md)
  The object responsible for the action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/discoverabilitytitle)*