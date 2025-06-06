# titleTextAttributes

**Framework**: UIKit  
**Kind**: property

String attributes to apply to the text of a standard-size title.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var titleTextAttributes: [NSAttributedString.Key : Any] { get set }
```

#### Discussion

If you don’t specify font or color attributes for the text, UIKit supplies appropriate default values. For a list of possible keys, see [`NSAttributedString.Key`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key).

## See Also

- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]](uinavigationbarappearance/largetitletextattributes.md)
  String attributes to apply to the text of a large-size title.
- [var titlePositionAdjustment: UIOffset](uinavigationbarappearance/titlepositionadjustment.md)
  The distance, in points, by which to offset the title horizontally and vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/titletextattributes)*