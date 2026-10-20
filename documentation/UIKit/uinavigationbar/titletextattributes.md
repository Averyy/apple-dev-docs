# titleTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Display attributes for the bar’s title text.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var titleTextAttributes: [NSAttributedString.Key : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * titleTextAttributes;
```

#### Discussion

You can specify the font, text color, text shadow color, and text shadow offset for the title in the text attributes dictionary, using the text attribute keys described in [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md).

## See Also

### Configuring the title
- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]?](./largetitletextattributes.md)
  Display attributes for the bar’s large title text.
- [func titleVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./titleverticalpositionadjustment%28for%29.md)
  Returns the title’s vertical position adjustment for given bar metrics.
- [func setTitleVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./settitleverticalpositionadjustment%28_,for%29.md)
  Sets the title’s vertical position adjustment for given bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/titletextattributes)*