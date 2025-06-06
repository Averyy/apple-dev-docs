# subtitle

**Framework**: UIKit  
**Kind**: property

The subtitle to display alongside the menu element’s title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var subtitle: String? { get set }
```

#### Discussion

Only the [`context`](uimenusystem/context.md) menu system supports the display of a subtitle, and only when the app is running on iOS.

## See Also

- [var title: String](uimenuelement/title.md)
  The title of the menu element.
- [var image: UIImage?](uimenuelement/image.md)
  The image to display alongside the menu element’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle)*