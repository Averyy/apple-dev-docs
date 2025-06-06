# image

**Framework**: UIKit  
**Kind**: property

The action’s image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var image: UIImage? { get set }
```

#### Discussion

The image appears next to the action’s [`title`](uiaction/title.md). Only the [`context`](uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

## See Also

- [var title: String](uiaction/title.md)
  The action’s title.
- [var identifier: UIAction.Identifier](uiaction/identifier-swift.property.md)
  The unique identifier for the action.
- [var discoverabilityTitle: String?](uiaction/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the action.
- [var attributes: UIMenuElement.Attributes](uiaction/attributes.md)
  The attributes indicating the style of the action.
- [var state: UIMenuElement.State](uiaction/state.md)
  The state of the action.
- [var sender: Any?](uiaction/sender.md)
  The object responsible for the action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/image)*