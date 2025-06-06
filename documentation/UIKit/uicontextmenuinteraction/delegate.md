# delegate

**Framework**: UIKit  
**Kind**: property

The object that provides the preview and contextual menu for your content and responds to interaction-related events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIContextMenuInteractionDelegate)? { get }
```

## See Also

- [protocol UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
  The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction/delegate)*