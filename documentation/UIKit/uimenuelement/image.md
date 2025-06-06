# image

**Framework**: UIKit  
**Kind**: property

The image to display alongside the menu element’s title.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var image: UIImage? { get }
```

#### Discussion

Only the [`context`](uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

## See Also

- [var title: String](uimenuelement/title.md)
  The title of the menu element.
- [var subtitle: String?](uimenuelement/subtitle.md)
  The subtitle to display alongside the menu element’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/image)*