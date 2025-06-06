# primaryAction

**Framework**: UIKit  
**Kind**: property

The launch scene’s primary action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@NSCopying
@MainActor var primaryAction: UIAction? { get set }
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Discussion

Set this property to customize the primary action’s button in the document launch scene. If you don’t set this property, the system adds a default Create Document button to the title view.

## See Also

- [var secondaryAction: UIAction?](uidocumentviewcontroller/launchoptions-swift.class/secondaryaction.md)
  The launch scene’s secondary action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class/primaryaction)*