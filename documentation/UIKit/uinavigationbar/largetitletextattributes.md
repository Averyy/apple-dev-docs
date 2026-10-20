# largeTitleTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Display attributes for the bar’s large title text.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var largeTitleTextAttributes: [NSAttributedString.Key : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * largeTitleTextAttributes;
```

#### Discussion

You can specify the font, text color, text shadow color, and text shadow offset for the title in the text attributes dictionary, using the text attribute keys described in [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md).

## See Also

### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]?](./titletextattributes.md)
  Display attributes for the bar’s title text.
- [func titleVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./titleverticalpositionadjustment%28for%29.md)
  Returns the title’s vertical position adjustment for given bar metrics.
- [func setTitleVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./settitleverticalpositionadjustment%28_,for%29.md)
  Sets the title’s vertical position adjustment for given bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/largetitletextattributes)*