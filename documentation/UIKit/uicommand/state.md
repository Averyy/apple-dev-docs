# state

**Framework**: UIKit  
**Kind**: property

The state of the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var state: UIMenuElement.State { get set }
```

## See Also

- [var title: String](uicommand/title.md)
  The command’s title.
- [var image: UIImage?](uicommand/image.md)
  The command’s image.
- [var action: Selector](uicommand/action.md)
  The selector identifying the action method called after the user selects the command.
- [var discoverabilityTitle: String?](uicommand/discoverabilitytitle.md)
  An elaborated title that explains the purpose of the command.
- [var attributes: UIMenuElement.Attributes](uicommand/attributes.md)
  The attributes indicating the style of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/state)*