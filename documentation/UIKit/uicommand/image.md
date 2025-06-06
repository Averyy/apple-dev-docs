# image

**Framework**: UIKit  
**Kind**: property

The command’s image.

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

Only the [`context`](uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

## See Also

- [var title: String](uicommand/title.md)
  The command’s title.
- [var action: Selector](uicommand/action.md)
  The selector identifying the action method called after the user selects the command.
- [var discoverabilityTitle: String?](uicommand/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the command.
- [var attributes: UIMenuElement.Attributes](uicommand/attributes.md)
  The attributes indicating the style of the command.
- [var state: UIMenuElement.State](uicommand/state.md)
  The state of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/image)*