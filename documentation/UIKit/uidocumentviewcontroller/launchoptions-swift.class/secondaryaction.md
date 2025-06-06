# secondaryAction

**Framework**: UIKit  
**Kind**: property

The launch scene’s secondary action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@NSCopying
@MainActor var secondaryAction: UIAction? { get set }
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Discussion

Set this property to add a secondary action to the document launch scene. If you set this property, the system adds a button for the secondary action to the title view.

## See Also

- [var primaryAction: UIAction?](uidocumentviewcontroller/launchoptions-swift.class/primaryaction.md)
  The launch scene’s primary action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/secondaryaction)*