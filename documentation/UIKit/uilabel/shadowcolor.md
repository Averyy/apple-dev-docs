# shadowColor

**Framework**: UIKit  
**Kind**: property

The shadow color of the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shadowColor: UIColor? { get set }
```

#### Discussion

The default value for this property is `nil`, which indicates that the text has no shadow. In addition to this property, you may also want to change the default shadow offset by modifying the [`shadowOffset`](uilabel/shadowoffset.md) property. A label draws its text shadows with the specified offset and color and no blurring.

## See Also

- [var shadowOffset: CGSize](uilabel/shadowoffset.md)
  The shadow offset, in points, for the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/shadowcolor)*