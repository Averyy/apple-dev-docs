# shadowOffset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The shadow offset, in points, for the text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var shadowOffset: CGSize { get set }
```

```objc
@property (nonatomic) CGSize shadowOffset;
```

## Discussion

The shadow color must be not be `nil` for this property to have any effect. The default offset size is `(0, -1)`, which indicates a shadow one point above the text. A label draws its text shadows with the specified offset and color and no blurring.

## See Also

### Drawing a shadow
- [var shadowColor: UIColor?](./shadowcolor.md)
  The shadow color of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/shadowoffset)*