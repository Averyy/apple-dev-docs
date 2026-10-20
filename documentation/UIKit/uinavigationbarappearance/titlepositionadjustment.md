# titlePositionAdjustment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The distance, in points, by which to offset the title horizontally and vertically.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var titlePositionAdjustment: UIOffset { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIOffset titlePositionAdjustment;
```

#### Discussion

Positive values move the title down and to the right. Negative values move the title up and to the left.

## See Also

### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]](./titletextattributes.md)
  String attributes to apply to the text of a standard-size title.
- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]](./largetitletextattributes.md)
  String attributes to apply to the text of a large-size title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/titlepositionadjustment)*