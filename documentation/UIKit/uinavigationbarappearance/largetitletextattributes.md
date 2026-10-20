# largeTitleTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

String attributes to apply to the text of a large-size title.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var largeTitleTextAttributes: [NSAttributedString.Key : Any] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSDictionary<NSString *,id> * largeTitleTextAttributes;
```

#### Discussion

If you don’t specify font or color attributes for the text, UIKit applies default font and color values. For a list of possible keys, see [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md).

## See Also

### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]](./titletextattributes.md)
  String attributes to apply to the text of a standard-size title.
- [var titlePositionAdjustment: UIOffset](./titlepositionadjustment.md)
  The distance, in points, by which to offset the title horizontally and vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/largetitletextattributes)*