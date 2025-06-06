# delegate

**Framework**: UIKit  
**Kind**: property

An object that acts as the delegate of the preview interaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPreviewInteractionDelegate)? { get set }
```

#### Discussion

The preview interaction informs the delegate of state and progress changes throughout the 3D Touch process. Create an object that conforms to the [`UIPreviewInteractionDelegate`](uipreviewinteractiondelegate.md) protocol and assign it to this property.

## See Also

- [protocol UIPreviewInteractionDelegate](uipreviewinteractiondelegate.md)
  A set of methods for communicating the progress of a preview interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteraction/delegate)*